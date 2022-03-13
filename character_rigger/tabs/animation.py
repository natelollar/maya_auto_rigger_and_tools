import maya.cmds as mc



    #_________________Animation Tab Methods ______________________#
    #_____________________________________________________________#
class animation_class():

    def multi_parent_const(self):
        mySel = mc.ls(sl=True)
        for i in mySel:
            if i != mySel[-1]:
                mc.parentConstraint(mySel[-1], i, mo=True, weight=True)

    def reset_ctrls(self):
        mySel = mc.ls(sl=True)
        for i in mySel:
            mc.setAttr((i + ".translate"), 0,0,0)
            mc.setAttr((i + ".rotate"), 0,0,0)
            mc.setAttr((i + ".scale"), 1,1,1)
        
    def create_locator(self):
        myLoc = mc.spaceLocator()
        mc.setAttr((myLoc[0] + ".overrideEnabled"), 1)
        mc.setAttr((myLoc[0] + ".overrideRGBColors"), 1)
        mc.setAttr((myLoc[0] + ".overrideColorRGB"), 1, 1, 0)
        mc.setAttr((myLoc[0] + ".localScale"), 15, 15, 15)
        mc.rename('temp_loc')

    def mirror_ctrls(self):
        #selection
        mySel = mc.ls(sl=True)
        #prefix text
        left_prefix = mc.textField('l_ctrlObject_text', query=True, text=True)
        right_prefix = mc.textField('r_ctrlObject_text', query=True, text=True)
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
            subVar = i.replace(left_prefix, right_prefix, 1) # '1', to replace first instance of string only
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