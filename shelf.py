bl_info = {
    "name": "Script Shelf",
    "author": "Rev",
    "version": (1, 0),
    "blender": (3, 0, 0),
    "location": "View3D > N-Panel > Shelf",
    "description": "Script shelfs",
    "category": "Development",
}

import bpy
import os
import json
from bpy.types import Panel, Operator, PropertyGroup
from bpy.props import StringProperty, IntProperty, CollectionProperty, PointerProperty
import pyperclip

def ensure_shelf_dir():
    scripts_dir = os.path.join(bpy.utils.user_resource('SCRIPTS'), "addons", "shelfscripts")
    if not os.path.exists(scripts_dir):
        os.makedirs(scripts_dir)
    return scripts_dir

def get_config_file():
    return os.path.join(ensure_shelf_dir(), "config.json")

def save_config(config):
    with open(get_config_file(), 'w') as f:
        json.dump(config, f)

def load_config():
    config_file = get_config_file()
    if os.path.exists(config_file):
        with open(config_file, 'r') as f:
            return json.load(f)
    default_config = {
        "panels": ["Script Shelf 1"],
        "current_panel": "Script Shelf 1",
        "orders": {"Script Shelf 1": []}
    }
    save_config(default_config)
    return default_config

def get_shelf_scripts(panel_name):
    scripts_dir = os.path.join(ensure_shelf_dir(), panel_name)
    if not os.path.exists(scripts_dir):
        os.makedirs(scripts_dir)
        
    files = [f[:-3] for f in os.listdir(scripts_dir) if f.endswith('.py')]
    config = load_config()
    order = config["orders"].get(panel_name, [])
    
    ordered_files = []
    for name in order:
        if name in files:
            ordered_files.append(name)
            files.remove(name)
    
    return ordered_files + files

class ShelfScriptProperties(PropertyGroup):
    script_index: IntProperty()

class SHELF_PT_Panel(Panel):
    bl_label = "Script Shelf"
    bl_idname = "VIEW3D_PT_shelf"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Shelf'

    def draw(self, context):
        layout = self.layout
        config = load_config()
        
        # Add panel button at top
        row = layout.row(align=True)
        row.alignment = 'RIGHT'
        row.operator("shelf.add_panel", text="Add Panel", icon='ADD')
        
        # Draw each sub-panel
        for panel_name in config["panels"]:
            box = layout.box()
            
            # Panel header
            header_row = box.row(align=True)
            
            # Expand/collapse arrow
            arrow = header_row.row()
            arrow.prop(context.scene.shelf_properties, f"expand_{panel_name}",
                        icon='TRIA_DOWN' if getattr(context.scene.shelf_properties, f"expand_{panel_name}", True) 
                        else 'TRIA_RIGHT',
                        icon_only=True, emboss=False)
            
            # Panel name (use operator to make clickable)
            op = header_row.operator("shelf.set_active_panel", text=panel_name, depress=(panel_name == config["current_panel"]))
            op.panel_name = panel_name
            
            # Panel management icons aligned right
            buttons_row = header_row.row(align=True)
            buttons_row.alignment = 'RIGHT'
            
            # Add script button
            paste_op = buttons_row.operator("shelf.paste_script", text="", icon='ADD')
            paste_op.panel_name = panel_name
            
            # Panel management buttons
            if len(config["panels"]) > 1:
                buttons_row.operator("shelf.remove_panel", text="", icon='REMOVE').panel_name = panel_name
            buttons_row.operator("shelf.rename_panel", text="", icon='GREASEPENCIL').panel_name = panel_name
            
            # Draw scripts if expanded
            if getattr(context.scene.shelf_properties, f"expand_{panel_name}", True):
                scripts = get_shelf_scripts(panel_name)
                    
                if scripts:
                    for idx, script in enumerate(scripts):
                        script_row = box.row(align=True)
                        script_row.separator(factor=1)  # Indent
                        script_row.operator("shelf.run_script", text=script).script_name = script
                        
                        ops_row = script_row.row(align=True)
                        ops_row.scale_x = 1
                        ops_row.alignment = 'RIGHT'
                        
                        ops_row.separator(factor=1)
                        rename_op = ops_row.operator("shelf.rename_script", text="", icon='GREASEPENCIL')
                        rename_op.script_name = script
                        rename_op.panel_name = panel_name
                        ops_row.separator(factor=1)
                                
                        if idx > 0:
                            up_op = ops_row.operator("shelf.move_script", text="", icon='TRIA_UP')
                            up_op.script_name = script
                            up_op.panel_name = panel_name
                            up_op.direction = 'UP'

                        if idx < len(scripts) - 1:
                            down_op = ops_row.operator("shelf.move_script", text="", icon='TRIA_DOWN')
                            down_op.script_name = script
                            down_op.panel_name = panel_name
                            down_op.direction = 'DOWN'
                        
                        ops_row.separator(factor=1)
                        del_op = ops_row.operator("shelf.delete_script", text="", icon='X')
                        del_op.script_name = script
                        del_op.panel_name = panel_name
                else:
                    box_row = box.row()
                    box_row.separator(factor=1)
                    box_row.label(text="No scripts added yet")
                    
                    
class SHELF_OT_add_panel(Operator):
    bl_idname = "shelf.add_panel"
    bl_label = "Add Panel"
    
    panel_name: StringProperty()
    def execute(self, context):
        config = load_config()
        new_number = len(config["panels"]) + 1
        new_name = f"Script Shelf {new_number}"
        config["panels"].append(new_name)
        config["orders"][new_name] = []
        save_config(config)
        return {'FINISHED'}

class SHELF_OT_set_active_panel(Operator):
    bl_idname = "shelf.set_active_panel"
    bl_label = "Set Active Panel"
    
    panel_name: StringProperty()
    
    def execute(self, context):
        config = load_config()
        config["current_panel"] = self.panel_name
        save_config(config)
        return {'FINISHED'}

class SHELF_OT_remove_panel(Operator):
    bl_idname = "shelf.remove_panel"
    bl_label = "Remove Current Panel"
    panel_name: StringProperty()
    def execute(self, context):
        config = load_config()
        if len(config["panels"]) > 1:
            current = config["current_panel"]
            config["panels"].remove(current)
            del config["orders"][current]
            config["current_panel"] = config["panels"][0]
            save_config(config)
            
            # Remove panel directory
            import shutil
            panel_dir = os.path.join(ensure_shelf_dir(), current)
            if os.path.exists(panel_dir):
                shutil.rmtree(panel_dir)
                
        return {'FINISHED'}

class SHELF_OT_rename_panel(Operator):
    bl_idname = "shelf.rename_panel"
    bl_label = "Rename Panel"
    
    new_name: StringProperty(name="New Name", default="Script Shelf")
    panel_name: StringProperty(options={'HIDDEN'})
    
    def execute(self, context):
        config = load_config()
        current = config["current_panel"]
        idx = config["panels"].index(current)
        
        # Rename directory
        old_dir = os.path.join(ensure_shelf_dir(), current)
        new_dir = os.path.join(ensure_shelf_dir(), self.new_name)
        if os.path.exists(old_dir):
            os.rename(old_dir, new_dir)
            
        # Update config
        config["panels"][idx] = self.new_name
        config["orders"][self.new_name] = config["orders"].pop(current)
        config["current_panel"] = self.new_name
        save_config(config)
        return {'FINISHED'}
        
    def invoke(self, context, event):
        config = load_config()
        self.new_name = config["current_panel"]
        return context.window_manager.invoke_props_dialog(self)

class SHELF_OT_switch_panel(Operator):
    bl_idname = "shelf.switch_panel"
    bl_label = "Switch Panel"
    
    panel_name: StringProperty()
    
    def execute(self, context):
        config = load_config()
        config["current_panel"] = self.panel_name
        save_config(config)
        return {'FINISHED'}

class SHELF_OT_paste_script(Operator):
    bl_idname = "shelf.paste_script"
    bl_label = "New Shelf Script"
    bl_options = {'REGISTER', 'UNDO'}
    
    script_name: StringProperty(name="Script Name", default="New Script")
    panel_name: StringProperty()

    def execute(self, context):
        try:
            script_content = pyperclip.paste()
            if not script_content.strip():
                self.report({'ERROR'}, "Clipboard is empty!")
                return {'CANCELLED'}
            
            config = load_config()
            current_panel = config["current_panel"]
            
            panel_dir = os.path.join(ensure_shelf_dir(), current_panel)
            if not os.path.exists(panel_dir):
                os.makedirs(panel_dir)
                
            script_path = os.path.join(panel_dir, f"{self.script_name}.py")
            
            with open(script_path, 'w') as f:
                f.write(script_content)
            
            if current_panel not in config["orders"]:
                config["orders"][current_panel] = []
                
            config["orders"][current_panel].append(self.script_name)
            save_config(config)
            
            return {'FINISHED'}
        except Exception as e:
            self.report({'ERROR'}, str(e))
            return {'CANCELLED'}

    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self)

class SHELF_OT_rename_script(Operator):
    bl_idname = "shelf.rename_script"
    bl_label = "Rename Script"
    bl_options = {'REGISTER', 'UNDO'}
    
    script_name: StringProperty(options={'HIDDEN'})
    new_name: StringProperty(name="New Name")
    panel_name: StringProperty(options={'HIDDEN'})
    target_panel: StringProperty(
        name="Panel",
        description="Target panel for the script"
    )

    def get_panels(self, context):
        config = load_config()
        return [(name, name, "") for name in config["panels"]]

    target_panel: bpy.props.EnumProperty(
        items=get_panels,
        name="Panel",
        description="Target panel for the script"
    )

    def execute(self, context):
        try:
            config = load_config()
            current_panel_dir = os.path.join(ensure_shelf_dir(), self.panel_name)
            target_panel_dir = os.path.join(ensure_shelf_dir(), self.target_panel)
            
            # Create target directory if it doesn't exist
            if not os.path.exists(target_panel_dir):
                os.makedirs(target_panel_dir)
            
            old_path = os.path.join(current_panel_dir, f"{self.script_name}.py")
            new_path = os.path.join(target_panel_dir, f"{self.new_name}.py")
            
            # Move and rename file
            os.rename(old_path, new_path)
            
            # Update orders in config
            # Remove from old panel
            if self.script_name in config["orders"][self.panel_name]:
                config["orders"][self.panel_name].remove(self.script_name)
            
            # Add to new panel
            if self.target_panel not in config["orders"]:
                config["orders"][self.target_panel] = []
            config["orders"][self.target_panel].append(self.new_name)
            
            save_config(config)
            return {'FINISHED'}
            
        except Exception as e:
            self.report({'ERROR'}, str(e))
            return {'CANCELLED'}

    def invoke(self, context, event):
        self.new_name = self.script_name
        self.target_panel = self.panel_name
        return context.window_manager.invoke_props_dialog(self)

    def draw(self, context):
        layout = self.layout
        layout.prop(self, "new_name")
        layout.prop(self, "target_panel")

class SHELF_OT_move_script(Operator):
    bl_idname = "shelf.move_script"
    bl_label = "Move Script"
    bl_options = {'REGISTER', 'UNDO'}
    
    script_name: StringProperty()
    direction: StringProperty()
    panel_name: StringProperty()

    def execute(self, context):
        config = load_config()
        current_panel = config["current_panel"]
        order = config["orders"][current_panel]
        
        if self.script_name not in order:
            order = get_shelf_scripts(current_panel)
            
        idx = order.index(self.script_name)
        if self.direction == 'UP' and idx > 0:
            order[idx], order[idx-1] = order[idx-1], order[idx]
        elif self.direction == 'DOWN' and idx < len(order) - 1:
            order[idx], order[idx+1] = order[idx+1], order[idx]
            
        config["orders"][current_panel] = order
        save_config(config)
        return {'FINISHED'}

class SHELF_OT_delete_script(Operator):
    bl_idname = "shelf.delete_script"
    bl_label = "Delete Script"
    bl_options = {'REGISTER', 'UNDO'}
    
    script_name: StringProperty()
    panel_name: StringProperty()

    def execute(self, context):
        try:
            config = load_config()
            current_panel = config["current_panel"]
            panel_dir = os.path.join(ensure_shelf_dir(), current_panel)
            script_path = os.path.join(panel_dir, f"{self.script_name}.py")
            
            os.remove(script_path)
            
            order = config["orders"][current_panel]
            if self.script_name in order:
                order.remove(self.script_name)
                save_config(config)
            
            return {'FINISHED'}
        except Exception as e:
            self.report({'ERROR'}, str(e))
            return {'CANCELLED'}

class SHELF_OT_run_script(Operator):
    bl_idname = "shelf.run_script"
    bl_label = "Run Shelf Script"
    bl_options = {'REGISTER', 'UNDO'}
    
    script_name: StringProperty()
    panel_name: StringProperty()

    def execute(self, context):
        try:
            config = load_config()
            current_panel = config["current_panel"]
            panel_dir = os.path.join(ensure_shelf_dir(), current_panel)
            script_path = os.path.join(panel_dir, f"{self.script_name}.py")
            
            with open(script_path, 'r') as f:
                script_content = f.read()
            
            exec(compile(script_content, script_path, 'exec'))
            return {'FINISHED'}
        except Exception as e:
            self.report({'ERROR'}, str(e))
            return {'CANCELLED'}

classes = (
    ShelfScriptProperties,
    SHELF_PT_Panel,
    SHELF_OT_paste_script,
    SHELF_OT_rename_script,
    SHELF_OT_move_script,
    SHELF_OT_delete_script,
    SHELF_OT_run_script,
    SHELF_OT_add_panel,
    SHELF_OT_remove_panel,
    SHELF_OT_rename_panel,
    SHELF_OT_switch_panel,
    SHELF_OT_set_active_panel,
)

def register():
    for cls in classes:
        bpy.utils.register_class(cls)
    bpy.types.Scene.shelf_properties = PointerProperty(type=ShelfScriptProperties)
    
    # Add expand properties for each panel
    config = load_config()
    for panel in config["panels"]:
        setattr(ShelfScriptProperties, f"expand_{panel}", 
                bpy.props.BoolProperty(default=True))

def unregister():
    # Remove dynamic properties
    config = load_config()
    for panel in config["panels"]:
        if hasattr(ShelfScriptProperties, f"expand_{panel}"):
            delattr(ShelfScriptProperties, f"expand_{panel}")
            
    for cls in classes:
        bpy.utils.unregister_class(cls)
    del bpy.types.Scene.shelf_properties

if __name__ == "__main__":
    register()
