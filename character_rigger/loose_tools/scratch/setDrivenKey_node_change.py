import maya.cmds as mc

#float is time, value is (2nd value, keyframe)
mc.setKeyframe('drivenKey_node', float=1, value=1)

mc.cutKey()