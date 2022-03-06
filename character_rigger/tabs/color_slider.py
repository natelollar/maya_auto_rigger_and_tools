import maya.cmds as mc

#_________________Color Tab Methods _________________________#
#____________________________________________________________#

class color_class():

    def slider_move(self):
        #query current slider value
        color1 = mc.intSlider('slider_value', q=True, value=True)
        #my selection
        mySel = mc.ls(sl=True)
        #apply color to selection shapes
        if color1 == 0: 
            mc.iconTextButton('color', e=True, bgc=(0.5, .5, 0.5))
            for i in mySel:
                selShape = mc.listRelatives(i, s=True)
                mc.setAttr((selShape[0] + ".overrideEnabled"), 0)
                mc.setAttr((selShape[0] + ".overrideRGBColors"), 0)
                mc.setAttr((selShape[0] + ".overrideColorRGB"), 0.5, 0.5, 0.5)
        if color1 == 1: 
            mc.iconTextButton('color', e=True, bgc=(.8, 0, .9))
            for i in mySel:
                selShape = mc.listRelatives(i, s=True)
                mc.setAttr((selShape[0] + ".overrideEnabled"), 1)
                mc.setAttr((selShape[0] + ".overrideRGBColors"), 1)
                mc.setAttr((selShape[0] + ".overrideColorRGB"), .8, 0, .9)
        if color1 == 2: 
            mc.iconTextButton('color', e=True, bgc=(1, .2, 0))
            for i in mySel:
                selShape = mc.listRelatives(i, s=True)
                mc.setAttr((selShape[0] + ".overrideEnabled"), 1)
                mc.setAttr((selShape[0] + ".overrideRGBColors"), 1)
                mc.setAttr((selShape[0] + ".overrideColorRGB"), 1, .2, 0)
        if color1 == 3: 
            mc.iconTextButton('color', e=True, bgc=(1, 1, 0))
            for i in mySel:
                selShape = mc.listRelatives(i, s=True)
                mc.setAttr((selShape[0] + ".overrideEnabled"), 1)
                mc.setAttr((selShape[0] + ".overrideRGBColors"), 1)
                mc.setAttr((selShape[0] + ".overrideColorRGB"), 1, 1, 0)
        if color1 == 4: 
            mc.iconTextButton('color', e=True, bgc=(0.6, 0, 0.15))
            for i in mySel:
                selShape = mc.listRelatives(i, s=True)
                mc.setAttr((selShape[0] + ".overrideEnabled"), 1)
                mc.setAttr((selShape[0] + ".overrideRGBColors"), 1)
                mc.setAttr((selShape[0] + ".overrideColorRGB"), 0.6, 0, 0.15)
        if color1 == 5: 
            mc.iconTextButton('color', e=True, bgc=(0, 0.9, 0))
            for i in mySel:
                selShape = mc.listRelatives(i, s=True)
                mc.setAttr((selShape[0] + ".overrideEnabled"), 1)
                mc.setAttr((selShape[0] + ".overrideRGBColors"), 1)
                mc.setAttr((selShape[0] + ".overrideColorRGB"), 0, .9, 0)

    #_______________________________#
    #change color of selection "TRANSFORM"
    #_______________________________#

    def transform_slider_move(self):
        #query current slider value
        color1 = mc.intSlider('transform_slider_value', q=True, value=True)
        #my selection
        mySel = mc.ls(sl=True)
        #apply color to selection shapes
        if color1 == 0: 
            mc.iconTextButton('transform_color', e=True, bgc=(0.5, .5, 0.5))
            for i in mySel:
                mc.setAttr((i + ".overrideEnabled"), 0)
                mc.setAttr((i + ".overrideRGBColors"), 0)
                mc.setAttr((i + ".overrideColorRGB"), 0.5, 0.5, 0.5)
        if color1 == 1: 
            mc.iconTextButton('transform_color', e=True, bgc=(.8, 0, .9))
            for i in mySel:
                mc.setAttr((i + ".overrideEnabled"), 1)
                mc.setAttr((i + ".overrideRGBColors"), 1)
                mc.setAttr((i + ".overrideColorRGB"), .8, 0, .9)
        if color1 == 2: 
            mc.iconTextButton('transform_color', e=True, bgc=(1, .2, 0))
            for i in mySel:
                mc.setAttr((i + ".overrideEnabled"), 1)
                mc.setAttr((i + ".overrideRGBColors"), 1)
                mc.setAttr((i + ".overrideColorRGB"), 1, .2, 0)
        if color1 == 3: 
            mc.iconTextButton('transform_color', e=True, bgc=(1, 1, 0))
            for i in mySel:
                mc.setAttr((i + ".overrideEnabled"), 1)
                mc.setAttr((i + ".overrideRGBColors"), 1)
                mc.setAttr((i + ".overrideColorRGB"), 1, 1, 0)
        if color1 == 4: 
            mc.iconTextButton('transform_color', e=True, bgc=(0.6, 0, 0.15))
            for i in mySel:
                mc.setAttr((i + ".overrideEnabled"), 1)
                mc.setAttr((i + ".overrideRGBColors"), 1)
                mc.setAttr((i + ".overrideColorRGB"), 0.6, 0, 0.15)
        if color1 == 5: 
            mc.iconTextButton('transform_color', e=True, bgc=(0, 0.9, 0))
            for i in mySel:
                mc.setAttr((i + ".overrideEnabled"), 1)
                mc.setAttr((i + ".overrideRGBColors"), 1)
                mc.setAttr((i + ".overrideColorRGB"), 0, .9, 0)


    #_______________________________#
    #change color of selection "WIRE" (Shape)
    #_______________________________#

    def wire_slider_move(self):
        #query current slider value
        color1 = mc.intSlider('wire_slider_value', q=True, value=True)
        #my selection
        mySel = mc.ls(sl=True)
        #apply color to selection shapes
        if color1 == 0: 
            mc.iconTextButton('wire_color', e=True, bgc=(0.5, .5, 0.5))
            for i in mySel:
                selShape = mc.listRelatives(i, s=True)
                mc.setAttr(selShape[0] + ".useObjectColor", 0)
                mc.setAttr(selShape[0] + ".wireColorRGB", 0, 0, 0)
        if color1 == 1: 
            mc.iconTextButton('wire_color', e=True, bgc=(.8, 0, .9))
            for i in mySel:
                selShape = mc.listRelatives(i, s=True)
                mc.setAttr(selShape[0] + ".useObjectColor", 2)
                mc.setAttr(selShape[0] + ".wireColorRGB", .8, 0, .9)
        if color1 == 2: 
            mc.iconTextButton('wire_color', e=True, bgc=(1, .2, 0))
            for i in mySel:
                selShape = mc.listRelatives(i, s=True)
                mc.setAttr(selShape[0] + ".useObjectColor", 2)
                mc.setAttr(selShape[0] + ".wireColorRGB", 1, .2, 0)
        if color1 == 3: 
            mc.iconTextButton('wire_color', e=True, bgc=(1, 1, 0))
            for i in mySel:
                selShape = mc.listRelatives(i, s=True)
                mc.setAttr(selShape[0] + ".useObjectColor", 2)
                mc.setAttr(selShape[0] + ".wireColorRGB", 1, 1, 0)
        if color1 == 4: 
            mc.iconTextButton('wire_color', e=True, bgc=(0.6, 0, 0.15))
            for i in mySel:
                selShape = mc.listRelatives(i, s=True)
                mc.setAttr(selShape[0] + ".useObjectColor", 2)
                mc.setAttr(selShape[0] + ".wireColorRGB", 0.6, 0, 0.15)
        if color1 == 5: 
            mc.iconTextButton('wire_color', e=True, bgc=(0, 0.9, 0))
            for i in mySel:
                selShape = mc.listRelatives(i, s=True)
                mc.setAttr(selShape[0] + ".useObjectColor", 2)
                mc.setAttr(selShape[0] + ".wireColorRGB", 0, 0.9, 0)


    #_______________________________#
    #change color of selection "WIRE" (Transform)
    #_______________________________#

    def wireT_slider_move(self):
        #query current slider value
        color1 = mc.intSlider('wireT_slider_value', q=True, value=True)
        #my selection
        mySel = mc.ls(sl=True)
        #apply color to selection shapes
        if color1 == 0: 
            mc.iconTextButton('wireT_color', e=True, bgc=(0.5, .5, 0.5))
            for i in mySel:
                mc.setAttr(i + ".useObjectColor", 0)
                mc.setAttr(i + ".wireColorRGB", 0, 0, 0)
        if color1 == 1: 
            mc.iconTextButton('wireT_color', e=True, bgc=(.8, 0, .9))
            for i in mySel:
                mc.setAttr(i + ".useObjectColor", 2)
                mc.setAttr(i + ".wireColorRGB", .8, 0, .9)
        if color1 == 2: 
            mc.iconTextButton('wireT_color', e=True, bgc=(1, .2, 0))
            for i in mySel:
                mc.setAttr(i + ".useObjectColor", 2)
                mc.setAttr(i + ".wireColorRGB", 1, .2, 0)
        if color1 == 3: 
            mc.iconTextButton('wireT_color', e=True, bgc=(1, 1, 0))
            for i in mySel:
                mc.setAttr(i + ".useObjectColor", 2)
                mc.setAttr(i + ".wireColorRGB", 1, 1, 0)
        if color1 == 4: 
            mc.iconTextButton('wireT_color', e=True, bgc=(0.6, 0, 0.15))
            for i in mySel:
                mc.setAttr(i + ".useObjectColor", 2)
                mc.setAttr(i + ".wireColorRGB", 0.6, 0, 0.15)
        if color1 == 5: 
            mc.iconTextButton('wireT_color', e=True, bgc=(0, 0.9, 0))
            for i in mySel:
                mc.setAttr(i + ".useObjectColor", 2)
                mc.setAttr(i + ".wireColorRGB", 0, 0.9, 0)


    #_______________________________#
    #Change Outliner color
    #_______________________________#

    def outliner_slider_move(self):
        #query current slider value
        color1 = mc.intSlider('outliner_slider_value', q=True, value=True)
        #my selection
        mySel = mc.ls(sl=True)
        #apply color to selection shapes
        if color1 == 0: 
            mc.iconTextButton('outliner_color', e=True, bgc=(0.5, .5, 0.5))
            for i in mySel:
                mc.setAttr(i + ".useOutlinerColor", 0)
                mc.setAttr(i + ".outlinerColor", 0, 0, 0)
        if color1 == 1: 
            mc.iconTextButton('outliner_color', e=True, bgc=(.8, 0, .9))
            for i in mySel:
                mc.setAttr(i + ".useOutlinerColor", 1)
                mc.setAttr(i + ".outlinerColor", .8, 0, .9)
        if color1 == 2: 
            mc.iconTextButton('outliner_color', e=True, bgc=(1, .2, 0))
            for i in mySel:
                mc.setAttr(i + ".useOutlinerColor", 1)
                mc.setAttr(i + ".outlinerColor", 1, .2, 0)
        if color1 == 3: 
            mc.iconTextButton('outliner_color', e=True, bgc=(1, 1, 0))
            for i in mySel:
                mc.setAttr(i + ".useOutlinerColor", 1)
                mc.setAttr(i + ".outlinerColor", 1, 1, 0)
        if color1 == 4: 
            mc.iconTextButton('outliner_color', e=True, bgc=(0.6, 0, 0.15))
            for i in mySel:
                mc.setAttr(i + ".useOutlinerColor", 1)
                mc.setAttr(i + ".outlinerColor", 0.6, 0, 0.15)
        if color1 == 5: 
            mc.iconTextButton('outliner_color', e=True, bgc=(0, 0.9, 0))
            for i in mySel:
                mc.setAttr(i + ".useOutlinerColor", 1)
                mc.setAttr(i + ".outlinerColor", 0, 0.9, 0)




