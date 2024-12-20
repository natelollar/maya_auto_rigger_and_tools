import maya.cmds as mc

#________

def outliner_move_up():
    mySel = mc.ls(sl=1)

    mc.reorder(mySel, relative=-1 )

def outliner_move_down():
    mySel = mc.ls(sl=1)

    mc.reorder(mySel, relative=1 )

#________

def outliner_move_up_five():
    mySel = mc.ls(sl=1)

    mc.reorder(mySel, relative=-5 )

def outliner_move_down_five():
    mySel = mc.ls(sl=1)

    mc.reorder(mySel, relative=5 )


#________
def outliner_select_down_one():
    mySel = mc.ls(sl=1)

    mc.pickWalk(mySel, direction='right') # right is down transform in group