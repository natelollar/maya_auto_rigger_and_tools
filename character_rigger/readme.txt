# first, put 'character_rigger' folder in root level of maya scripts folder
# C:\Users\Bob\Documents\maya\2020\scripts

# 'ar' stands for 'auto rig'
# launch 'rigger_ui.py' in 'ar_ui' folder

# launch 'rigger_ui' with this python code:

import character_rigger
character_rigger.ar_ui.rigger_ui.rigger_ui_class().rigger_ui_method()

# make a shelf button by middle mouse dragging this code to a maya shelf from the script editor
    # (also the launch script is in the 'launch_ui' file)

# if maya has trouble importing files, use the 'import_reload' file to import and reload all files 
    # ( you could make a shelf button of this too ) 