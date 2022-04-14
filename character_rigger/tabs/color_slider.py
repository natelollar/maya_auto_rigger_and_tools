import maya.cmds as mc

#_________________Color Tab Methods _________________________#
#____________________________________________________________#

class color_class():

    #_______________________________#
    #change color of selection "Shape/s"
    #_______________________________#
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
                for shape in selShape:
                    mc.setAttr((shape + ".overrideEnabled"), 0)
                    mc.setAttr((shape + ".overrideRGBColors"), 0)
                    mc.setAttr((shape + ".overrideColorRGB"), 0.5, 0.5, 0.5)
        if color1 == 1: 
            mc.iconTextButton('color', e=True, bgc=(.8, 0, .9))
            for i in mySel:
                selShape = mc.listRelatives(i, s=True)
                for shape in selShape:
                    mc.setAttr((shape + ".overrideEnabled"), 1)
                    mc.setAttr((shape + ".overrideRGBColors"), 1)
                    mc.setAttr((shape + ".overrideColorRGB"), .8, 0, .9)
        if color1 == 2: 
            mc.iconTextButton('color', e=True, bgc=(1, .2, 0))
            for i in mySel:
                selShape = mc.listRelatives(i, s=True)
                for shape in selShape:
                    mc.setAttr((shape + ".overrideEnabled"), 1)
                    mc.setAttr((shape + ".overrideRGBColors"), 1)
                    mc.setAttr((shape + ".overrideColorRGB"), 1, .2, 0)
        if color1 == 3: 
            mc.iconTextButton('color', e=True, bgc=(1, 1, 0))
            for i in mySel:
                selShape = mc.listRelatives(i, s=True)
                for shape in selShape:
                    mc.setAttr((shape + ".overrideEnabled"), 1)
                    mc.setAttr((shape + ".overrideRGBColors"), 1)
                    mc.setAttr((shape + ".overrideColorRGB"), 1, 1, 0)
        if color1 == 4: 
            mc.iconTextButton('color', e=True, bgc=(0.6, 0, 0.15))
            for i in mySel:
                selShape = mc.listRelatives(i, s=True)
                for shape in selShape:
                    mc.setAttr((shape + ".overrideEnabled"), 1)
                    mc.setAttr((shape + ".overrideRGBColors"), 1)
                    mc.setAttr((shape + ".overrideColorRGB"), 0.6, 0, 0.15)
        if color1 == 5: 
            mc.iconTextButton('color', e=True, bgc=(0, .7, 0))
            for i in mySel:
                selShape = mc.listRelatives(i, s=True)
                for shape in selShape:
                    mc.setAttr((shape + ".overrideEnabled"), 1)
                    mc.setAttr((shape + ".overrideRGBColors"), 1)
                    mc.setAttr((shape + ".overrideColorRGB"), 0, .7, 0)
        if color1 == 6: 
            mc.iconTextButton('color', e=True, bgc=(1, 0, 0))
            for i in mySel:
                selShape = mc.listRelatives(i, s=True)
                for shape in selShape:
                    mc.setAttr((shape + ".overrideEnabled"), 1)
                    mc.setAttr((shape + ".overrideRGBColors"), 1)
                    mc.setAttr((shape + ".overrideColorRGB"), 1, 0, 0)
        if color1 == 7: 
            mc.iconTextButton('color', e=True, bgc=(0, 1, 0))
            for i in mySel:
                selShape = mc.listRelatives(i, s=True)
                for shape in selShape:
                    mc.setAttr((shape + ".overrideEnabled"), 1)
                    mc.setAttr((shape + ".overrideRGBColors"), 1)
                    mc.setAttr((shape + ".overrideColorRGB"), 0, 1, 0)
        if color1 == 8: 
            mc.iconTextButton('color', e=True, bgc=(0, 0, 1))
            for i in mySel:
                selShape = mc.listRelatives(i, s=True)
                for shape in selShape:
                    mc.setAttr((shape + ".overrideEnabled"), 1)
                    mc.setAttr((shape + ".overrideRGBColors"), 1)
                    mc.setAttr((shape + ".overrideColorRGB"), 0, 0, 1)
        if color1 == 9: 
            mc.iconTextButton('color', e=True, bgc=(0, 1, 1))
            for i in mySel:
                selShape = mc.listRelatives(i, s=True)
                for shape in selShape:
                    mc.setAttr((shape + ".overrideEnabled"), 1)
                    mc.setAttr((shape + ".overrideRGBColors"), 1)
                    mc.setAttr((shape + ".overrideColorRGB"), 0, 1, 1)
        if color1 == 10: 
            mc.iconTextButton('color', e=True, bgc=(1, 0, 1))
            for i in mySel:
                selShape = mc.listRelatives(i, s=True)
                for shape in selShape:
                    mc.setAttr((shape + ".overrideEnabled"), 1)
                    mc.setAttr((shape + ".overrideRGBColors"), 1)
                    mc.setAttr((shape + ".overrideColorRGB"), 1, 0, 1)
        if color1 == 11: 
            mc.iconTextButton('color', e=True, bgc=(.5, 0, 1))
            for i in mySel:
                selShape = mc.listRelatives(i, s=True)
                for shape in selShape:
                    mc.setAttr((shape + ".overrideEnabled"), 1)
                    mc.setAttr((shape + ".overrideRGBColors"), 1)
                    mc.setAttr((shape + ".overrideColorRGB"), .5, 0, 1)
        if color1 == 12: 
            mc.iconTextButton('color', e=True, bgc=(.5, 1, 0))
            for i in mySel:
                selShape = mc.listRelatives(i, s=True)
                for shape in selShape:
                    mc.setAttr((shape + ".overrideEnabled"), 1)
                    mc.setAttr((shape + ".overrideRGBColors"), 1)
                    mc.setAttr((shape + ".overrideColorRGB"), .5, 1, 0)
        if color1 == 13: 
            mc.iconTextButton('color', e=True, bgc=(0, .5, 1))
            for i in mySel:
                selShape = mc.listRelatives(i, s=True)
                for shape in selShape:
                    mc.setAttr((shape + ".overrideEnabled"), 1)
                    mc.setAttr((shape + ".overrideRGBColors"), 1)
                    mc.setAttr((shape + ".overrideColorRGB"), 0, .5, 1)
        if color1 == 14: 
            mc.iconTextButton('color', e=True, bgc=(0, .25, 1))
            for i in mySel:
                selShape = mc.listRelatives(i, s=True)
                for shape in selShape:
                    mc.setAttr((shape + ".overrideEnabled"), 1)
                    mc.setAttr((shape + ".overrideRGBColors"), 1)
                    mc.setAttr((shape + ".overrideColorRGB"), 0, .25, 1)
        
        


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
            mc.iconTextButton('transform_color', e=True, bgc=(0, .7, 0))
            for i in mySel:
                mc.setAttr((i + ".overrideEnabled"), 1)
                mc.setAttr((i + ".overrideRGBColors"), 1)
                mc.setAttr((i + ".overrideColorRGB"), 0, .7, 0)
        if color1 == 6: 
            mc.iconTextButton('transform_color', e=True, bgc=(1, 0, 0))
            for i in mySel:
                mc.setAttr((i + ".overrideEnabled"), 1)
                mc.setAttr((i + ".overrideRGBColors"), 1)
                mc.setAttr((i + ".overrideColorRGB"), 1, 0, 0)
        if color1 == 7: 
            mc.iconTextButton('transform_color', e=True, bgc=(0, 1, 0))
            for i in mySel:
                mc.setAttr((i + ".overrideEnabled"), 1)
                mc.setAttr((i + ".overrideRGBColors"), 1)
                mc.setAttr((i + ".overrideColorRGB"), 0, 1, 0)
        if color1 == 8: 
            mc.iconTextButton('transform_color', e=True, bgc=(0, 0, 1))
            for i in mySel:
                mc.setAttr((i + ".overrideEnabled"), 1)
                mc.setAttr((i + ".overrideRGBColors"), 1)
                mc.setAttr((i + ".overrideColorRGB"), 0, 0, 1)
        if color1 == 9: 
            mc.iconTextButton('transform_color', e=True, bgc=(0, 1, 1))
            for i in mySel:
                mc.setAttr((i + ".overrideEnabled"), 1)
                mc.setAttr((i + ".overrideRGBColors"), 1)
                mc.setAttr((i + ".overrideColorRGB"), 0, 1, 1)
        if color1 == 10: 
            mc.iconTextButton('transform_color', e=True, bgc=(1, 0, 1))
            for i in mySel:
                mc.setAttr((i + ".overrideEnabled"), 1)
                mc.setAttr((i + ".overrideRGBColors"), 1)
                mc.setAttr((i + ".overrideColorRGB"), 1, 0, 1)
        if color1 == 11: 
            mc.iconTextButton('transform_color', e=True, bgc=(.5, 0, 1))
            for i in mySel:
                mc.setAttr((i + ".overrideEnabled"), 1)
                mc.setAttr((i + ".overrideRGBColors"), 1)
                mc.setAttr((i + ".overrideColorRGB"), .5, 0, 1)


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
            mc.iconTextButton('wire_color', e=True, bgc=(0, .7, 0))
            for i in mySel:
                selShape = mc.listRelatives(i, s=True)
                mc.setAttr(selShape[0] + ".useObjectColor", 2)
                mc.setAttr(selShape[0] + ".wireColorRGB", 0, .7, 0)
        if color1 == 6: 
            mc.iconTextButton('wire_color', e=True, bgc=(1, 0, 0))
            for i in mySel:
                selShape = mc.listRelatives(i, s=True)
                mc.setAttr(selShape[0] + ".useObjectColor", 2)
                mc.setAttr(selShape[0] + ".wireColorRGB", 1, 0, 0)
        if color1 == 7: 
            mc.iconTextButton('wire_color', e=True, bgc=(0, 1, 0))
            for i in mySel:
                selShape = mc.listRelatives(i, s=True)
                mc.setAttr(selShape[0] + ".useObjectColor", 2)
                mc.setAttr(selShape[0] + ".wireColorRGB", 0, 1, 0)
        if color1 == 8: 
            mc.iconTextButton('wire_color', e=True, bgc=(0, 0, 1))
            for i in mySel:
                selShape = mc.listRelatives(i, s=True)
                mc.setAttr(selShape[0] + ".useObjectColor", 2)
                mc.setAttr(selShape[0] + ".wireColorRGB", 0, 0, 1)
        if color1 == 9: 
            mc.iconTextButton('wire_color', e=True, bgc=(0, 1, 1))
            for i in mySel:
                selShape = mc.listRelatives(i, s=True)
                mc.setAttr(selShape[0] + ".useObjectColor", 2)
                mc.setAttr(selShape[0] + ".wireColorRGB", 0, 1, 1)
        if color1 == 10: 
            mc.iconTextButton('wire_color', e=True, bgc=(1, 0, 1))
            for i in mySel:
                selShape = mc.listRelatives(i, s=True)
                mc.setAttr(selShape[0] + ".useObjectColor", 2)
                mc.setAttr(selShape[0] + ".wireColorRGB", 1, 0, 1)
        if color1 == 11: 
            mc.iconTextButton('wire_color', e=True, bgc=(.5, 0, 1))
            for i in mySel:
                selShape = mc.listRelatives(i, s=True)
                mc.setAttr(selShape[0] + ".useObjectColor", 2)
                mc.setAttr(selShape[0] + ".wireColorRGB", .5, 0, 1)


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
            mc.iconTextButton('wireT_color', e=True, bgc=(0, .7, 0))
            for i in mySel:
                mc.setAttr(i + ".useObjectColor", 2)
                mc.setAttr(i + ".wireColorRGB", 0, .7, 0)
        if color1 == 6: 
            mc.iconTextButton('wireT_color', e=True, bgc=(1, 0, 0))
            for i in mySel:
                mc.setAttr(i + ".useObjectColor", 2)
                mc.setAttr(i + ".wireColorRGB", 1, 0, 0)
        if color1 == 7: 
            mc.iconTextButton('wireT_color', e=True, bgc=(0, 1, 0))
            for i in mySel:
                mc.setAttr(i + ".useObjectColor", 2)
                mc.setAttr(i + ".wireColorRGB", 0, 1, 0)
        if color1 == 8: 
            mc.iconTextButton('wireT_color', e=True, bgc=(0, 0, 1))
            for i in mySel:
                mc.setAttr(i + ".useObjectColor", 2)
                mc.setAttr(i + ".wireColorRGB", 0, 0, 1)
        if color1 == 9: 
            mc.iconTextButton('wireT_color', e=True, bgc=(0, 1, 1))
            for i in mySel:
                mc.setAttr(i + ".useObjectColor", 2)
                mc.setAttr(i + ".wireColorRGB", 0, 1, 1)
        if color1 == 10: 
            mc.iconTextButton('wireT_color', e=True, bgc=(1, 0, 1))
            for i in mySel:
                mc.setAttr(i + ".useObjectColor", 2)
                mc.setAttr(i + ".wireColorRGB", 1, 0, 1)
        if color1 == 11: 
            mc.iconTextButton('wireT_color', e=True, bgc=(.5, 0, 1))
            for i in mySel:
                mc.setAttr(i + ".useObjectColor", 2)
                mc.setAttr(i + ".wireColorRGB", .5, 0, 1)


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
            mc.iconTextButton('outliner_color', e=True, bgc=(0, .7, 0))
            for i in mySel:
                mc.setAttr(i + ".useOutlinerColor", 1)
                mc.setAttr(i + ".outlinerColor", 0, .7, 0)
        if color1 == 6: 
            mc.iconTextButton('outliner_color', e=True, bgc=(1, 0, 0))
            for i in mySel:
                mc.setAttr(i + ".useOutlinerColor", 1)
                mc.setAttr(i + ".outlinerColor", 1, 0, 0)
        if color1 == 7: 
            mc.iconTextButton('outliner_color', e=True, bgc=(0, 1, 0))
            for i in mySel:
                mc.setAttr(i + ".useOutlinerColor", 1)
                mc.setAttr(i + ".outlinerColor", 0, 1, 0)
        if color1 == 8: 
            mc.iconTextButton('outliner_color', e=True, bgc=(0, 0, 1))
            for i in mySel:
                mc.setAttr(i + ".useOutlinerColor", 1)
                mc.setAttr(i + ".outlinerColor", 0, 0, 1)
        if color1 == 9: 
            mc.iconTextButton('outliner_color', e=True, bgc=(0, 1, 1))
            for i in mySel:
                mc.setAttr(i + ".useOutlinerColor", 1)
                mc.setAttr(i + ".outlinerColor", 0, 1, 1)
        if color1 == 10: 
            mc.iconTextButton('outliner_color', e=True, bgc=(1, 0, 1))
            for i in mySel:
                mc.setAttr(i + ".useOutlinerColor", 1)
                mc.setAttr(i + ".outlinerColor", 1, 0, 1)
        if color1 == 11: 
            mc.iconTextButton('outliner_color', e=True, bgc=(.5, 0, 1))
            for i in mySel:
                mc.setAttr(i + ".useOutlinerColor", 1)
                mc.setAttr(i + ".outlinerColor", .5, 0, 1)

    
    def curve_width(self):
        #query current slider value
        curveW = mc.intSlider('curve_width_value', q=True, value=True)
        #my selection
        mySel = mc.ls(sl=True)
        # to avoid red error when nothing selected
        if mySel:
            #apply color to selection shapes
            if curveW == 0: 
                mc.iconTextButton('curve_width', e=True, bgc=(0, 0, 0))
                for i in mySel:
                    selShape = mc.listRelatives(i, s=True)
                    for i in selShape:
                        mc.setAttr(i + ".lineWidth", -1)
            if curveW == 1: 
                mc.iconTextButton('curve_width', e=True, bgc=(0.1, 0.1, 0.1))
                for i in mySel:
                    selShape = mc.listRelatives(i, s=True)
                    for i in selShape:
                        mc.setAttr(i + ".lineWidth", 1.5)
            if curveW == 2: 
                mc.iconTextButton('curve_width', e=True, bgc=(0.2, 0.2, 0.2))
                for i in mySel:
                    selShape = mc.listRelatives(i, s=True)
                    for i in selShape:
                        mc.setAttr(i + ".lineWidth", 2)
            if curveW == 3: 
                mc.iconTextButton('curve_width', e=True, bgc=(0.3, 0.3, 0.3))
                for i in mySel:
                    selShape = mc.listRelatives(i, s=True)
                    for i in selShape:
                        mc.setAttr(i + ".lineWidth", 3)
            if curveW == 4: 
                mc.iconTextButton('curve_width', e=True, bgc=(0.4, 0.4, 0.4))
                for i in mySel:
                    selShape = mc.listRelatives(i, s=True)
                    for i in selShape:
                        mc.setAttr(i + ".lineWidth", 4)
            if curveW == 5: 
                mc.iconTextButton('curve_width', e=True, bgc=(0.5, 0.5, 0.5))
                for i in mySel:
                    selShape = mc.listRelatives(i, s=True)
                    for i in selShape:
                        mc.setAttr(i + ".lineWidth", 5)
            if curveW == 6: 
                mc.iconTextButton('curve_width', e=True, bgc=(0.6, 0.6, 0.6))
                for i in mySel:
                    selShape = mc.listRelatives(i, s=True)
                    for i in selShape:
                        mc.setAttr(i + ".lineWidth", 6)
            if curveW == 7: 
                mc.iconTextButton('curve_width', e=True, bgc=(0.7, 0.7, 0.7))
                for i in mySel:
                    selShape = mc.listRelatives(i, s=True)
                    for i in selShape:
                        mc.setAttr(i + ".lineWidth", 7)
            if curveW == 8: 
                mc.iconTextButton('curve_width', e=True, bgc=(0.8, 0.8, 0.8) )
                for i in mySel:
                    selShape = mc.listRelatives(i, s=True)
                    for i in selShape:
                        mc.setAttr(i + ".lineWidth", 8)
            if curveW == 9: 
                mc.iconTextButton('curve_width', e=True, bgc=(0.9, 0.9, 0.9))
                for i in mySel:
                    selShape = mc.listRelatives(i, s=True)
                    for i in selShape:
                        mc.setAttr(i + ".lineWidth", 9)
            if curveW == 10: 
                mc.iconTextButton('curve_width', e=True, bgc=(0.95, 0.95, 0.95))
                for i in mySel:
                    selShape = mc.listRelatives(i, s=True)
                    for i in selShape:
                        mc.setAttr(i + ".lineWidth", 10)
            if curveW == 11: 
                mc.iconTextButton('curve_width', e=True, bgc=(1, 1, 1))
                for i in mySel:
                    selShape = mc.listRelatives(i, s=True)
                    for i in selShape:
                        mc.setAttr(i + ".lineWidth", 11)

            curve_width = mc.getAttr(selShape[0] + ".lineWidth")

            # print width for user to know
            if curve_width:
                print(curve_width)
        else:
            print('Please select curve! Nothing selected.')


