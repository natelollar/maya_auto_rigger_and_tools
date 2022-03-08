import maya.cmds as mc



    #_________________Auto Rig Tab Options _______________________#
    #_____________________________________________________________#

class auto_rig_options():

    def auto_rig_options(self):
        # lowest jnts in y of upper face jnts
        midFace_jnt_amnt = mc.textField('midFace_jnt_amnt_text', query=True, text=True)
        pass

    '''
    def midFace_jnt_amount(self):
        #selection
        mySel = mc.ls(sl=True)
        #prefix text
        left_prefix = mc.textField('l_hip_text', query=True, text=True)
        right_prefix = mc.textField('r_hip_text', query=True, text=True)
        #multiplier text
        tranX_mult = mc.textField('translateX_text', query=True, text=True)
        tranY_mult = mc.textField('translateY_text', query=True, text=True)
        tranZ_mult = mc.textField('translateZ_text', query=True, text=True)
        rotX_mult = mc.textField('rotateX_text', query=True, text=True)
        rotY_mult = mc.textField('rotateY_text', query=True, text=True)
        rotZ_mult = mc.textField('rotateZ_text', query=True, text=True)

        #mirrioring values of ctrls with correct prefix
        for i in mySel:
            #switching L_R_ prefix
            subVar = i.replace(left_prefix, right_prefix)
            mc.copyAttr(i, subVar, values=True, attribute=('translate', 'rotate', 'scale'))

            #get values of right side to multiply offset
            subVarTX = mc.getAttr(subVar + '.translateX')
            subVarTY = mc.getAttr(subVar + '.translateY')
            subVarTZ = mc.getAttr(subVar + '.translateZ')
            subVarRX = mc.getAttr(subVar + '.rotateX')
            subVarRY = mc.getAttr(subVar + '.rotateY')
            subVarRZ = mc.getAttr(subVar + '.rotateZ')
            # multiply trans, and rotation, by text fields to reverse etc
            mc.setAttr((subVar + '.translateX'), (subVarTX * float(tranX_mult)))
            mc.setAttr((subVar + '.translateY'), (subVarTY * float(tranY_mult)))
            mc.setAttr((subVar + '.translateZ'), (subVarTZ * float(tranZ_mult)))
            mc.setAttr((subVar + '.rotateX'), (subVarRX * float(rotX_mult)))
            mc.setAttr((subVar + '.rotateY'), (subVarRY * float(rotY_mult)))
            mc.setAttr((subVar + '.rotateZ'), (subVarRZ * float(rotZ_mult)))

        #set focus back to maya
        mc.setFocus('MayaWindow')

    
    def ctrl_sizes(self):
        pass

    def head_jnts(self):
        # tongue, bot face, top face, ears, eyes

        # flatten ankle and toe rev foot ctrls

        # x down the chain  (might not matter that much, except), checkbox or radio button

        # save ctrl shapes

        #save example skeletons that work, reproduce in 1 click



        #___________definatley 

        # rev toe placement, button, error "already exist"

        # ctrl size (global), text field, global multiplier

        # mid face jnt amount, text field

        # picture or words of requirements (wrist parented to elbow, (though shouldn't need) need tongue)
                #or could have an option if wrist is parented to elbow

        # maybe, head or no head
            # could just skip all head ctrls if no head, would positions still work?

        # checkbox, head or no head


        pass
    '''