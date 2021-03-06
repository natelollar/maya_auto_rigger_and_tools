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
            try:
                mc.setAttr((i + ".translate"), 0,0,0)
            except:
                pass
            try:
                mc.setAttr((i + ".rotate"), 0,0,0)
            except:
                pass
            try:
                mc.setAttr((i + ".scale"), 1,1,1)
            except:
                pass
        
    def create_locator(self):
        myLoc = mc.spaceLocator()
        mc.setAttr((myLoc[0] + ".overrideEnabled"), 1)
        mc.setAttr((myLoc[0] + ".overrideRGBColors"), 1)
        mc.setAttr((myLoc[0] + ".overrideColorRGB"), 1, 1, 0)
        mc.setAttr((myLoc[0] + ".localScale"), 15, 15, 15)
        mc.rename('temp_loc')

    def mirror_ctrls(self, row='1'):
        #selection
        mySel = mc.ls(sl=True)
        if row == 1:
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
        if row == 2:
            #prefix text
            left_prefix = mc.textField('l_ctrlObject_textA', query=True, text=True)
            right_prefix = mc.textField('r_ctrlObject_textA', query=True, text=True)
            #multiplier text
            tranX_mult = mc.textField('translateX_textA', query=True, text=True)
            tranY_mult = mc.textField('translateY_textA', query=True, text=True)
            tranZ_mult = mc.textField('translateZ_textA', query=True, text=True)
            rotX_mult = mc.textField('rotateX_textA', query=True, text=True)
            rotY_mult = mc.textField('rotateY_textA', query=True, text=True)
            rotZ_mult = mc.textField('rotateZ_textA', query=True, text=True)
        if row == 3:
            #prefix text
            left_prefix = mc.textField('l_ctrlObject_textB', query=True, text=True)
            right_prefix = mc.textField('r_ctrlObject_textB', query=True, text=True)
            #multiplier text
            tranX_mult = mc.textField('translateX_textB', query=True, text=True)
            tranY_mult = mc.textField('translateY_textB', query=True, text=True)
            tranZ_mult = mc.textField('translateZ_textB', query=True, text=True)
            rotX_mult = mc.textField('rotateX_textB', query=True, text=True)
            rotY_mult = mc.textField('rotateY_textB', query=True, text=True)
            rotZ_mult = mc.textField('rotateZ_textB', query=True, text=True)

        #mirrioring values of ctrls with correct prefix
        for i in mySel:
            #switching L_R_ prefix
            subVar = i.replace(left_prefix, right_prefix, 1) # '1', to replace first instance of string only
            # transfer attributes over to opposite side
            mc.copyAttr(i, subVar, values=True, attribute=('translate', 'rotate', 'scale'))

            #get values of right side to multiply offset
            subVarTX = mc.getAttr(subVar + '.translateX')
            subVarTY = mc.getAttr(subVar + '.translateY')
            subVarTZ = mc.getAttr(subVar + '.translateZ')
            subVarRX = mc.getAttr(subVar + '.rotateX')
            subVarRY = mc.getAttr(subVar + '.rotateY')
            subVarRZ = mc.getAttr(subVar + '.rotateZ')
            # multiply trans, and rotation, by text fields to reverse etc
            try:
                mc.setAttr((subVar + '.translateX'), (subVarTX * float(tranX_mult)))
            except:
                pass
            try:
                mc.setAttr((subVar + '.translateY'), (subVarTY * float(tranY_mult)))
            except:
                pass
            try:
                mc.setAttr((subVar + '.translateZ'), (subVarTZ * float(tranZ_mult)))
            except:
                pass
            try:
                mc.setAttr((subVar + '.rotateX'), (subVarRX * float(rotX_mult)))
            except:
                pass
            try:
                mc.setAttr((subVar + '.rotateY'), (subVarRY * float(rotY_mult)))
            except:
                pass
            try:
                mc.setAttr((subVar + '.rotateZ'), (subVarRZ * float(rotZ_mult)))
            except:
                pass

        #set focus back to maya
        mc.setFocus('MayaWindow')