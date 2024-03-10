# --------------------- SAVE ANIM ATTRIBUTES --------------------- #
# Works well as shelf buttons.
import maya.cmds as cmds
import json
from pathlib import Path
import ast

# select animation controls
# save current frame translate, rotate, scale of selected controls
class SaveAnimAttributes:

    def __init__(self, file_name="anim_attributes.json", file_location=""):
        print(
            "# ----------------------------- BEGIN ----------------------------- #"
        )
        self.file_name = file_name
        self.file_location = file_location

    def __del__(self):
        print(
            "# ----------------------------- END ----------------------------- #"
        )

    # Default save location is downloads folder.
    def save_location(self):
        if self.file_location == "":
            home = Path.home()
            downloads = home / "Downloads"
            return downloads
        else:
            return self.file_location

    # ------------------------------------------------------------------------------------------- #
    # --------------------------- GET ATTRIBUTES AND WRITE TO JSON FILE ------------------------- #
    def get_anim_attributes(self):
        anim_attributes = {}

        my_sel = cmds.ls(sl=True)

        for object in my_sel:
            translate = cmds.getAttr(f"{object}.translate")
            rotate = cmds.getAttr(f"{object}.rotate")
            scale = cmds.getAttr(f"{object}.scale")

            anim_attributes[object] = {
                'translate': str(translate),
                'rotate': str(rotate),
                'scale': str(scale),
            }

        return anim_attributes

    # Write anim attributes to json.
    def write_anim_attributes_to_file(self):
        file_path = f"{self.save_location()}\{self.file_name}"
        with open(file_path, 'w') as file:
            json.dump(self.get_anim_attributes(), file, indent=4)
            print(f"File saved to...  {file_path}")

    # --------------------------------------------------------------------------------- #
    # --------------------------- LOAD IN AND APPLY JSON FILE ------------------------- #
    # Read json file.
    def read_anim_attributes_file(self):
        file_path = f"{self.save_location()}\{self.file_name}"
        with open(file_path, 'r') as file:
            data = json.load(file)
            print(f"File read from...  {file_path}")
            return data

    def apply_anim_attributes(self):
        # Iterate through anim attributes.
        # Apply to controls or objects.
        for object, attr_list in self.read_anim_attributes_file().items():
            # Import anim attributes from json file.
            # Use ast.literal_eval() to convert string back to regular data.
            trans_attr = ast.literal_eval(attr_list['translate'])[0]
            rot_attr = ast.literal_eval(attr_list['rotate'])[0]
            scale_attr = ast.literal_eval(attr_list['scale'])[0]

            if cmds.objExists(object):
                try:
                    cmds.setAttr(f"{object}.translate", trans_attr[0], trans_attr[1], trans_attr[2])
                    print(f"{object}.translate set to {trans_attr}")
                except:
                    print(f"{object}.translate LOCKED!")
                try:
                    cmds.setAttr(f"{object}.rotate", rot_attr[0], rot_attr[1], rot_attr[2])
                    print(f"{object} rotate set to {rot_attr}")
                except:
                    print(f"{object}.rotate LOCKED!")    
                try:
                    cmds.setAttr(f"{object}.scale", scale_attr[0], scale_attr[1], scale_attr[2])
                    print(f"{object} scale set to {scale_attr}")
                except:
                    print(f"{object}.scale LOCKED!")  

# --------------------------- RUN METHODS --------------------------- #
# WRITE ATTRIBUTES OUT
# SELECT ANIM CONTROLS OR OBJECTS
#SaveAnimAttributes().write_anim_attributes_to_file()

# APPLY ANIM ATTRIBUES
# NO SELECTION REQUIRED
#SaveAnimAttributes().apply_anim_attributes()
