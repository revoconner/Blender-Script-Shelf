# Blender Scripts Shelf
### Add to shelf from context menu is in Alpha (Has a megathread in the issue tab, report bugs there)
### The rest of the script is in Beta, works well but can encounter non critical bugs from time to time. 
### If you encounter bugs, please report
A blender add-on for having custom scripts on a shelf, like maya's shelf or 3ds max custom toolbar.
Just copy and paste your scripts here to create buttons to run them later.

Organise them, rename them or sort them in the order you want.</br></br>
<img width="400" alt="image" src="https://github.com/user-attachments/assets/2e53b130-fe57-4bfe-aaf5-9f5b157447e8"> </br></br>
Learnt blender last week and can't believe it lacks the basic function to store scripts in a custom shelf.</br>
But it's as close as I could get to a working shelf that doesn't require user to deal with files and folders during use. </br>
No need to add create folders, add scripts manually or play around with folder structures. Everything is automated!

# Contents
1. [Features](https://github.com/revoconner/Blender-Script-Shelf/edit/main/README.md#contents)
2. [Video Tutorial and Demo](https://github.com/revoconner/Blender-Script-Shelf/blob/main/README.md#video-tutorial-and-demo)
3. [Installation](https://github.com/revoconner/Blender-Script-Shelf/blob/main/README.md#installation)
4. [Use](https://github.com/revoconner/Blender-Script-Shelf/blob/main/README.md#use)
5. [Note](https://github.com/revoconner/Blender-Script-Shelf/blob/main/README.md#note)
6. [Changelog](https://github.com/revoconner/Blender-Script-Shelf/blob/main/README.md#changelog)

## Features
1. Copy and paste script to shelves. As close as drag and drop as it can get. </br></br>
<img width="400" alt="image" src="https://github.com/user-attachments/assets/d1d35c19-79c0-4ca4-8dd4-637f952a7a53"> </br>
</br>
2. Reorder them, rename them from within blender. </br> Organise and reorder the shelf, subpanel, items. Move items between subpanels.</br></br>
<img width="400" alt="image" src="https://github.com/user-attachments/assets/a0af6180-4f69-4c66-bcb2-7f97edc31928"> </br>
</br>
3. Edit saved scripts from within blender.</br></br>
<img width="600" alt="image" src="https://github.com/user-attachments/assets/0a096278-45ab-4d2c-9929-76ae371297cb"> </br>
</br>
4. Add blender in-built items to the shelve with right click and add to shelf.</br></br>
<img width="400" alt="image" src="https://github.com/user-attachments/assets/dee0ae9e-284c-49aa-ab13-362c8e438b06"> </br>
</br>
5. Remove a panel, or delete a script </br></br>
<img width="400" alt="image" src="https://github.com/user-attachments/assets/234346c1-4bdf-4b1d-b100-c528bc31b34a"> </br>
</br>
6. Shelves can be backed up between blender installations.</br>
Just save **%appdata%\Blender Foundation\Blender\4.2\scripts\addons** somewhere

## Video Tutorial and Demo
Youtube Video: https://youtu.be/zgCNfnMXQSc 

**The demo lacks Update 1.1 additions, that were added after the demo was recorded:**
1. Editing exist script function has been added but not shown in demo.
2. Add existing menu items from blender to the shelf for quick access. No mention of this in the demo.

See [Changelog](https://github.com/revoconner/Blender-Script-Shelf/blob/main/README.md#changelog), for better understanding. These settings have been explained in [Use](https://github.com/revoconner/Blender-Script-Shelf/blob/main/README.md#use) section.

## Installation
1. Run blender as administrator and open the install_dependencies.py file in the script editor, run it. (First time use only, or on new blender install) </br> This will install pyperclip module in the blender python lib-packages. If you do not run as admin, the module will install in the user lib-package directory that blender doesn't have on path. Thanks to luckychris for making this script. </br> <img width="700" alt="image" src="https://github.com/user-attachments/assets/247aa44a-3c22-4a91-af36-edf0d74b3725">

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
2. Added the ability to edit saved scripts from within blender.
3. Bug Fixes
