
import maya.cmds as cmds

#drag materials into hypershade from windows explorer
#grab base color texture, or grab all textures

def arnold_basic_add_connections():  
    
    mySel = cmds.ls(sl=True)

    for i in mySel:
        if "_BaseColor_1" in i: #only use Base_Color to get base material name
            tex_nm = i.replace("_BaseColor_1", "")  #texture name, without the Base_Color_1 text

            myColor = tex_nm + "_BaseColor_1"
            myAOMetalRough = tex_nm + "_OcclusionRoughnessMetallic_1"
            myNormal = tex_nm + "_Normal_1"
            myEmissive = tex_nm + "_Emissive_1"

        color_correct_node = cmds.shadingNode ( 'aiColorCorrect', n = 'aiColorCorrect_' + tex_nm + "_BaseColor_1", asUtility=True)
        cmds.connectAttr(myColor + ".outColor", color_correct_node + ".input", force=True) 
        cmds.connectAttr(color_correct_node + ".outColor", "aiLayerRgba_" + tex_nm + "_BaseColor_1" + ".input8", force=True) 