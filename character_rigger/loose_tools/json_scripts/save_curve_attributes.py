import maya.cmds as cmds
import json
from pathlib import Path

class SaveCurveAttributes:
    def __init__(self, file_name="curve_attributes.json", file_location=""):
        print("# ----------------------------- BEGIN ----------------------------- #")
        self.file_name = file_name
        self.file_location = file_location

    def __del__(self):
        print("# ----------------------------- END ----------------------------- #")

    def save_location(self):
        if self.file_location=="":
            home = Path.home()
            downloads = home / "Downloads"
            return downloads
        else:
            return self.file_location

    # --------------------------- GET ATTRIBUTES AND WRITE TO JSON FILE ------------------------- #
    def get_curve_attributes(self):
        curve_attributes = {}

        my_sel = cmds.ls(sl=True)

        for curve in my_sel:
            # Select curve transforms, not shapes.
            curve_shapes = cmds.listRelatives(curve, shapes=True)

            for shape in curve_shapes:
                #print(shape)
                if cmds.objectType(shape) == 'nurbsCurve':
                    color = cmds.getAttr(f"{shape}.overrideColorRGB")
                    color_alpha = cmds.getAttr(f"{shape}.overrideColorA")
                    lineWidth = cmds.getAttr(f"{shape}.lineWidth")
                    #print(color)
                    #print(color_alpha)
                    #print(lineWidth)
    
                    curve_attributes[shape] = {
                        'color': color,
                        'color_alpha': color_alpha,
                        'lineWidth': lineWidth
                    }
        
        return curve_attributes

    def write_curve_attributes_to_file(self): 
        file_path=f"{self.save_location()}\{self.file_name}"
        with open(file_path, 'w') as file:
            json.dump(self.get_curve_attributes(), file, indent=4)
            print(f"File saved to...  {file_path}")

    # --------------------------- LOAD IN AND APPLY JSON FILE ------------------------- #
    def read_curve_attributes_file(self):
        file_path = f"{self.save_location()}\{self.file_name}"
        with open(file_path, 'r') as file:
            data = json.load(file)
            print(f"File read from...  {file_path}")
            return data

    def apply_curve_attributes(self):
        for shape, attr_list in self.read_curve_attributes_file().items():
            print(shape)

            shape_colorR = attr_list['color'][0][0]
            shape_colorG = attr_list['color'][0][1]
            shape_colorB = attr_list['color'][0][2]
            shape_colorA = attr_list['color_alpha']
            shape_lineWidth = attr_list['lineWidth']
            print(shape_colorR, shape_colorG, shape_colorB)
            print(shape_colorA)
            print(shape_lineWidth)

            if cmds.objExists(shape):
                cmds.setAttr(f"{shape}.overrideEnabled", 1)
                cmds.setAttr(f"{shape}.overrideRGBColors", 1)
                cmds.setAttr(f"{shape}.overrideColorRGB", shape_colorR, shape_colorG, shape_colorB)
                cmds.setAttr(f"{shape}.overrideColorA", shape_colorA)
                cmds.setAttr(f"{shape}.lineWidth", shape_lineWidth)
            else:
                print((f"Shape does not exist!: {shape}"))



# --------------------------- RUN METHODS --------------------------- #
# WRITE ATTRIBUTES OUT
# SELECT CURVE TRANSFORMS
#SaveCurveAttributes().write_curve_attributes_to_file()

# APPLY CURVE COLOR AND WIDTH
# NO SELECTION REQUIRED
#SaveCurveAttributes().apply_curve_attributes()