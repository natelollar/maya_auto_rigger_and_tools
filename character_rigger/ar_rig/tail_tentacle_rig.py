import maya.cmds as mc

from ..ar_functions import sel_near_jnt
from ..ar_functions import sel_joints


def tail_tentacle_rig(jnt_prefix = 'sknJnt_'):
    #spineRoot_jnt = sel_near_jnt.sel_near_jnt('standin_obj_spine_root')
    tailStart_jnt = sel_near_jnt.sel_near_jnt('standin_obj_tail_start')
    tailEnd_jnt = sel_near_jnt.sel_near_jnt('standin_obj_tail_end')
    print(tailStart_jnt)
    print(tailEnd_jnt)
    #spineRoot_ctrl_nm0 = spineRoot_jnt[0].replace(jnt_prefix, '')
    #spineRoot_ctrl_nm1 = spineRoot_ctrl_nm0 + '_ctrl'

    # select joint chain
    jnt_chain = sel_joints.sel_joints(tailStart_jnt[0], tailEnd_jnt[0]).rev_sel_jnt_chainA()
    print(jnt_chain)
    mc.select(cl=1)
    mc.select(jnt_chain)

    #print(spineRoot_jnt)
    #print(spineRoot_ctrl_nm1)