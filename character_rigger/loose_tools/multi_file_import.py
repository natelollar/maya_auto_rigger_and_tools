import maya.cmds as mc
from pathlib import Path

model_path_dir = mc.fileDialog2(fileMode=4, #4 Then names of one or more existing files.
                                caption='Choose Redshift Proxies',
                                dialogStyle=2,
                                okCaption='Accept')
#print (model_path_dir)

for i in model_path_dir:
    name = Path(i).stem
    #path = pathlib.PurePath(i)
    print (name)



import maya.cmds as mc

sel = mc.ls(selection=True)

#attr = mc.listAttr(sel)

#print(attr)

mc.setAttr(sel[0] + '.fileName', 'D:\Videos\redshift_proxy\Castle_Wall_sbfw6_LOD0.rs', type='string')