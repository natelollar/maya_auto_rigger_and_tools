# --------------------- SAVE CURVE ATTRIBUTES --------------------- #
# Works well as shelf buttons.
import maya.cmds as cmds
import json
from pathlib import Path
import ast

# Select controls (transforms) and use write_curve_attributes_to_file() to save out curve attributes.
# Use apply_curve_attributes() to load back in json. No selection required.
# Saves out curve shape color, color alpha, line width, and cv shape.
# Should work with regular cv curves and circles.
class SaveCurveAttributes:
    def __init__(self, file_name="curve_attributes.json", file_location=""):
        print("# ----------------------------- BEGIN ----------------------------- #")
        self.file_name = file_name
        self.file_location = file_location

    def __del__(self):
        print("# ----------------------------- END ----------------------------- #")

    # Default save location is downloads folder.
    def save_location(self):
        if self.file_location=="":
            home = Path.home()
            downloads = home / "Downloads"
            return downloads
        else:
            return self.file_location

    # ------------------------------------------------------------------------------------------- #
    # --------------------------- GET ATTRIBUTES AND WRITE TO JSON FILE ------------------------- #
    def get_curve_attributes(self):
        curve_attributes = {}

        my_sel = cmds.ls(sl=True)

        for curve in my_sel:
            # Select curve transforms, not shapes.
            curve_shapes = cmds.listRelatives(curve, shapes=True)

            for shape in curve_shapes:
                if cmds.objectType(shape) == "nurbsCurve":
                    curve_transform = curve
                    color = cmds.getAttr(f"{shape}.overrideColorRGB")
                    color_alpha = cmds.getAttr(f"{shape}.overrideColorA")
                    lineWidth = cmds.getAttr(f"{shape}.lineWidth")

                    curve_degree = cmds.getAttr(f"{shape}.degree")
                    curve_spans = cmds.getAttr(f"{shape}.spans")
                    curve_form = cmds.getAttr(f"{shape}.form")
                    #curve_minValue = cmds.getAttr(f"{shape}.minValue")
                    #curve_maxValue = cmds.getAttr(f"{shape}.maxValue")

                    cv_positions = cmds.getAttr(f"{shape}.cv[*]")
                    #cv_pos_index = f"{shape}.cv[*]"

                    curveInfo_node = cmds.createNode('curveInfo', n = "temporary_curveInfo")
                    cmds.connectAttr( f"{shape}.worldSpace", f"{curveInfo_node}.inputCurve")
                    curve_knots = cmds.getAttr(f"{curveInfo_node}.knots[*]")
                    #curve_points = cmds.getAttr(f"{curveInfo_node}.controlPoints[*]")

                    cmds.delete(curveInfo_node)

                    curve_attributes[shape] = {
                        'curve_transform': curve_transform,
                        'color': str(color),
                        'color_alpha': color_alpha,
                        'lineWidth': lineWidth,
                        'curve_degree': curve_degree,
                        'curve_spans': curve_spans,
                        'curve_form': curve_form,
                        'cv_positions': str(cv_positions),
                        'curve_knots': str(curve_knots),
                    }

        return curve_attributes

    # Write curve attributes to json.
    def write_curve_attributes_to_file(self): 
        file_path=f"{self.save_location()}\{self.file_name}"
        with open(file_path, 'w') as file:
            json.dump(self.get_curve_attributes(), file, indent=4)
            print(f"File saved to...  {file_path}")

    # --------------------------------------------------------------------------------- #
    # --------------------------- LOAD IN AND APPLY JSON FILE ------------------------- #
    # Read json file.
    def read_curve_attributes_file(self):
        file_path = f"{self.save_location()}\{self.file_name}"
        with open(file_path, 'r') as file:
            data = json.load(file)
            print(f"File read from...  {file_path}")
            return data

    def apply_curve_attributes(self):
        old_shape_list = []
        curve_transform_list = []
        # Iterate through curve shape data.
        # Apply to control curves.  
        # Replace current control or create new ones if curve shape transforms don't exist.
        for shape, attr_list in self.read_curve_attributes_file().items():
            curve_transform = attr_list['curve_transform']

            old_shape_list.append(shape) # Append to delete leftover shapes from previous version.
            curve_transform_list.append(curve_transform)

            # Import curve attributes from json file.
            # Use ast.literal_eval() to convert string back to regular data.
            shape_colorR = ast.literal_eval(attr_list['color'])[0][0]
            shape_colorG = ast.literal_eval(attr_list['color'])[0][1]
            shape_colorB = ast.literal_eval(attr_list['color'])[0][2]
            shape_colorA = attr_list['color_alpha']
            shape_lineWidth = attr_list['lineWidth']

            curve_degree = attr_list['curve_degree']
            curve_spans = attr_list['curve_spans']
            curve_form = attr_list['curve_form']
            cv_positions = ast.literal_eval(attr_list['cv_positions'])
            #curve_knots = ast.literal_eval(attr_list['curve_knots'])

            if cmds.objExists(curve_transform):
                trans_nd = curve_transform
            else:
                trans_nd = cmds.group(em=True, name=curve_transform)
            # Empty shape so transform group acts as a 'shape transform' and not a 'group'.
            em_curve_shp = cmds.createNode('nurbsCurve', name=f"{shape}_empty_shape", parent=trans_nd)
           
            if cmds.objExists(shape):  # Delete and replace old shapes incase shape has entirely changed.
                cmds.delete(shape) 

            # Create new curve shapes.  Account for different forms of curve shapes including circles.   
            # Generally speaking this is a regular control curve drawn out with CV Curve Tool.
            if curve_form == 0 or curve_form == 1:
                new_curve_trans = cmds.curve(point=cv_positions, degree=curve_degree)
                new_curve_shp = cmds.listRelatives(new_curve_trans, shapes=True)
            # Generally speaking this is a blocky circle with straight sharp edges. 
            # Like a regular curve but starts out as a closed shape.  Can be built with cmds.circle(degree==1).   
            # Delete history off circles or will not work.
            if curve_form == 2 and curve_degree == 1:  # Closed curve and degree is linear.  
                last_element = cv_positions.pop() # Last cv position to first to form a closed curve.
                cv_positions.insert(0, last_element)
                new_curve_trans = cmds.curve(point=cv_positions, degree=curve_degree)
                new_curve_shp = cmds.listRelatives(new_curve_trans, shapes=True)
            # Generally speaking a regular smooth circle.
            if curve_form == 2 and curve_degree != 1: # Closed periodic curve shape and degree is cubic (smooth).
                new_curve_trans = cmds.circle(sections=curve_spans, degree=curve_degree, constructionHistory=False) # Spans should be same as sections.
                new_curve_shp = cmds.listRelatives(new_curve_trans, shapes=True)[0]
                for cv_index, pos in enumerate(cv_positions):  #cmds.curve() would not work with smooth circle.
                    cv_identifier = f"{new_curve_shp}.cv[{cv_index}]"
                    cmds.xform(cv_identifier, translation=pos)
            
            # Parent curve shape to control transform node.
            cmds.parent(new_curve_shp, trans_nd, relative=True, shape=True)
            cmds.rename(new_curve_shp, shape)
            cmds.delete(new_curve_trans)

            # APPLY CONTROL CURVE COLOR, ALPHA, & WIDTH
            if cmds.objExists(shape):
                cmds.setAttr(f"{shape}.overrideEnabled", 1)
                cmds.setAttr(f"{shape}.overrideRGBColors", 1)
                cmds.setAttr(f"{shape}.overrideColorRGB", shape_colorR, shape_colorG, shape_colorB)
                cmds.setAttr(f"{shape}.overrideColorA", shape_colorA)
                cmds.setAttr(f"{shape}.lineWidth", shape_lineWidth)
            else:
                cmds.warning(f"Shape still does not exist!!!:  {shape}")

        # Remove empty shape and shapes not saved out in json file.  
        # Remove shapes not in new version of controls.
        for curve_transform in curve_transform_list:
            current_shapes = cmds.listRelatives(curve_transform, shapes=True) 
            for crv_shp in current_shapes:
                if crv_shp not in old_shape_list:
                    cmds.delete(crv_shp)
        
        # Clear last selection.
        cmds.select(clear=True)

# --------------------------- RUN METHODS --------------------------- #
# WRITE ATTRIBUTES OUT
# SELECT CURVE TRANSFORMS
#SaveCurveAttributes().write_curve_attributes_to_file()

# APPLY CURVE COLOR AND WIDTH
# NO SELECTION REQUIRED
#SaveCurveAttributes().apply_curve_attributes()