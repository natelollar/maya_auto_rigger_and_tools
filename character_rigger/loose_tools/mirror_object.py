from maya import cmds

print('------------- START -----------------')

my_sel = cmds.ls(selection=True)

# mirror selected object
for object in my_sel:
    object_tx_mult = -1
    object_ty_mult = 1
    object_tz_mult = 1
    object_rx_mult = 1
    object_ry_mult = -1
    object_rz_mult = -1

    for attr in 'tr':
        for axis in 'xyz':
            mult_value = globals()[f'object_{attr}{axis}_mult']
            objectAttr = objectTX = cmds.getAttr(object + f'.{attr}{axis}')
            cmds.setAttr(object + f'.{attr}{axis}', (objectAttr * mult_value))

print('------------- END -----------------')