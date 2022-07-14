import maya.cmds as mc

proxy_node = mc.createNode('RedshiftProxyMesh', name='rsProxy_node')

shp_node = mc.createNode('mesh')

mc.sets(e=True, forceElement='initialShadingGroup')

mc.connectAttr(proxy_node + '.outMesh', shp_node + '.inMesh')

trans_node0 = mc.listRelatives(shp_node, parent=True)
trans_node = mc.rename(trans_node0, 'rsProxy')
