# Open blender as administrator
# Paste this script or open it in the scripting panel inside blender
# Run it
# Wait for a few seconds
# You will only need to do this once every new installation of blender
# Thanks to luckychris for making this script. 

import sys
import subprocess
import os
import platform
import bpy

def isWindows():
    return os.name == 'nt'

def isMacOS():
    return os.name == 'posix' and platform.system() == "Darwin"

def isLinux():
    return os.name == 'posix' and platform.system() == "Linux"

def python_exec():
    
    if isWindows():
        import sys
        return os.path.join(sys.prefix, 'bin', 'python.exe')
    elif isMacOS():
        import sys
        try:
            # 2.92 and older
            path = bpy.app.binary_path_python
        except AttributeError:
            # 2.93 and later
            path = sys.executable
        return os.path.abspath(path)
    elif isLinux():
        import sys
        return os.path.join(sys.prefix, 'bin', 'python3.11')
    else:
        print("sorry, still not implemented for ", os.name, " - ", platform.system)


def installModule(packageName):
    python_exe = python_exec()
    subprocess.call([python_exe, "-m", "pip", "install", packageName])
        
installModule("pyperclip")
