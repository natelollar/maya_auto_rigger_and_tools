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
        my_sel_name = [object.split('|')[-1] for object in my_sel]

        for object in my_sel_name:
            translate = cmds.getAttr(f"{object}.translate")[0]
            translate_round = [round(float, 6) for float in translate]

            rotate = cmds.getAttr(f"{object}.rotate")[0]
            rotate_round = [round(float, 6) for float in rotate]
            
            scale = cmds.getAttr(f"{object}.scale")[0]
            scale_round = [round(float, 6) for float in scale]
            
            joint_orient = cmds.getAttr(f"{object}.jointOrient")[0]
            joint_orient_round = [round(float, 6) for float in joint_orient]

            anim_attributes[object] = {
                'translate': str(translate_round),
                'rotate': str(rotate_round),
                'scale': str(scale_round),
                'joint_orient': str(joint_orient_round),
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
            trans_attr = ast.literal_eval(attr_list['translate'])
            rot_attr = ast.literal_eval(attr_list['rotate'])
            scale_attr = ast.literal_eval(attr_list['scale'])
            jnt_ori_attr = ast.literal_eval(attr_list['joint_orient'])

            if cmds.objExists(object):
                try:
                    cmds.setAttr(f"{object}.translate", trans_attr[0],
                                 trans_attr[1], trans_attr[2])
                    print(f"{object}.translate set to {trans_attr}")
                except:
                    print(f"{object}.translate SKIPPED. May be locked.")
                try:
                    cmds.setAttr(f"{object}.rotate", rot_attr[0], rot_attr[1],
                                 rot_attr[2])
                    print(f"{object}.rotate set to {rot_attr}")
                except:
                    print(f"{object}.rotate SKIPPED. May be locked.")
                try:
                    cmds.setAttr(f"{object}.scale", scale_attr[0],
                                 scale_attr[1], scale_attr[2])
                    print(f"{object}.scale set to {scale_attr}")
                except:
                    print(f"{object}.scale SKIPPED. May be locked.")
                try:
                    cmds.setAttr(f"{object}.jointOrient", jnt_ori_attr[0],
                                 jnt_ori_attr[1], jnt_ori_attr[2])
                    print(f"{object}.jointOrient set to {jnt_ori_attr}")
                except:
                    print(f"{object}.jointOrient SKIPPED. May be locked.")

# --------------------------- RUN METHODS --------------------------- #
# WRITE ATTRIBUTES OUT
# SELECT ANIM CONTROLS OR OBJECTS
#SaveAnimAttributes().write_anim_attributes_to_file()

# APPLY ANIM ATTRIBUES
# NO SELECTION REQUIRED
#SaveAnimAttributes().apply_anim_attributes()
