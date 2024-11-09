# Blender Scripts Shelf
#### Alpha - Expect minor bugs
A blender add-on for having custom scripts on a shelf, like maya's shelf or 3ds max custom toolbar.
Just copy and paste your scripts here to create buttons to run them later.

Organise them, rename them or sort them in the order you want.

Learnt blender last week and can't believe it lacks the basic function to store scripts in a custom shelf. So I created this, it's nto pretty and you cannot drag and drop scripts directly from the script editor, which is a bummer. But it's as close as I could get to a working shelf that doesn't require user to deal with files and folders during use.

## Video Tutorial and Demo
Youtube Video: https://youtu.be/zgCNfnMXQSc 

**The demo lacks a few things that were added after the demo was recorded:**
1. Editing exist script function has been added but not shown in demo.
2. Add existing menu items from blender to the shelf for quick access. No mention of this in the demo.

#### Script Panel
<img width="400" alt="image" src="https://github.com/user-attachments/assets/2ab84a03-fb2d-4bb9-9e42-ee787d96694f"> </br>
#### Add New Script (Copies clipboard content into the script)
<img width="377" alt="image" src="https://github.com/user-attachments/assets/0846f3d0-eaaf-44da-8891-19b8351920d7"> </br>
#### Rename script or move it to another panel
<img width="377" alt="image" src="https://github.com/user-attachments/assets/fe678fce-12e5-4b89-b22c-6dea837a0944"> </br>
#### Remove a panel
<img width="400" alt="image" src="https://github.com/user-attachments/assets/3c98f75b-b47d-4bba-9afc-77af7b763f06"> </br>
#### Editing saved script directly in blender. (No more messing around in folders) - UPDATE 1.1
Click the icon underlines to open the script in the inbuilt text editor. Save the script to save changes.
<img width="400" alt="image" src="https://github.com/user-attachments/assets/ec738c23-6c1e-4054-abd7-88f1b21e28f3"> </br>
#### Add blender items to the shelf for quick access - UPDATE 1.1
<img width="400" alt="image" src="https://github.com/user-attachments/assets/241dffc2-673d-452c-bf14-d577794771d1"> </br>

## Installation
1. Run blender as administrator and open the install_dependencies.py file in the script editor, run it. (First time use only, or on new blender install) </br> This will install pyperclip module in the blender python lib-packages. If you do not run as admin, the module will install in the user lib-package directory that blender doesn't have on path. Thanks to luckychris for making this script. </br> <img width="500" alt="image" src="https://github.com/user-attachments/assets/247aa44a-3c22-4a91-af36-edf0d74b3725">

2. Install the shelf.py as an add on. </br> <img width="300" alt="image" src="https://github.com/user-attachments/assets/c8400d7c-1bca-4dc0-9772-851c8954e563">

## Use
1. Open shelf main panel from the N-Panel
2. Create or rename panels with the pencil icon.
3. Delete panels with the cross icon
4. To add a script, first copy it from a text editor or blender script editor. Then click the + icon. This will save the script with the name you specify and paste the content of your clipboard into the button that is created.
5. To run a saved script just click on the shelf button.
6. To move a script from one panel to another, click on the pencil icon. You can rename here or move it to another panel.
7. To edit a saved script, click the edit script button right next to the name. This will open the script in the inbuilt text editor inside blender, save the script to save the changes.
8. You can now add blender's inbuilt items to the shelf for quick access. Use the context menu on items, and select add to shelf option. It's added by default to blender items subpanel but can be renamed and moved.

## Note
1. Depends on the pyperclip module.
2. Can be a little slow to update the interface in between rename and add operations. (bug)
3. Could have been prettier to look at, probably will be in the future releases.
4. Please post any bugs or issues so I can solve them.
5. To remove all traces of the add-on, uninstall the add-on then delete the shelfscript folder from the user add-on folder for blender. **%appdata%\Blender Foundation\Blender\4.2\scripts\addons**
6. Only tested on Windows 11 on Blender 4.2.2

## Changelog
#### 09/11/24 
Initial Commit

#### 10/11/24
Update 1.1 
1. Added "Add to shelf" function to blender inbuilt items. Tools are not yet supported.
2. Added the ability to edit sasved scripts from within blender.
