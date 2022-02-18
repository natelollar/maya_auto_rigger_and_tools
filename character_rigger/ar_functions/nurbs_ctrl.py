# create nurbs control, parent contrain to joint

import maya.cmds as mc

class nurbs_ctrl():
    def __init__(self, name, size, colorR, colorG, colorB):
        self.name = name
        self.size = size
        self.colorR = colorR
        self.colorG = colorG
        self.colorB = colorB

    def box_ctrl(self):
        print('_____AAAAAA______')
        print(self.name)
        print(self.colorR)
        print('_____AAAAAA______')

    def circle_ctrl(self):
        # create and name nurbs curve
        nurbsCurve = mc.circle( n=(self.name), ch=False, r=10, nr=(1,0,0) )
        mc.setAttr( (nurbsCurve[0] + '.scale'), self.size, self.size, self.size )
        mc.makeIdentity(apply=True)
        itemsShape = mc.listRelatives(s=True)
        mc.setAttr( (itemsShape[0] + '.overrideEnabled'), 1 )
        mc.setAttr( (itemsShape[0] + '.overrideRGBColors'), 1 )
        mc.setAttr( (itemsShape[0] + '.overrideColorRGB'), self.colorR, self.colorG, self.colorB )

        # grp nurbs curve control
        curveGroup = mc.group( nurbsCurve, n=(self.name + '_grp') )
        curveGroup_offset = mc.group( nurbsCurve, n=(self.name + '_grp_offset') )

        # return name of control and its grp
        return curveGroup, nurbsCurve[0]

    def global_ctrl(self):
        # create and name nurbs curve
        nurbsCurve = mc.curve( n=(self.name), d=1, p=[  (5.0, 0.0, 110.0),
                                                        (75.0, 0.0, 45.0),
                                                        (85.0, 0.0, 15.0),
                                                        (80.0, 0.0, -30.0),
                                                        (60.0, 0.0, -50.0),
                                                        (-60.0, 0.0, -50.0),
                                                        (-80.0, 0.0, -30.0),
                                                        (-85.0, 0.0, 15.0),
                                                        (-75.0, 0.0, 45.0),
                                                        (-5.0, 0.0, 110.0),
                                                        (5.0, 0.0, 110.0)
                                                        ])
        mc.setAttr( (nurbsCurve + '.scale'), self.size, self.size, self.size )
        mc.makeIdentity(apply=True)

        itemsShape = mc.listRelatives(s=True)
        mc.setAttr( (itemsShape[0] + '.overrideEnabled'), 1 )
        mc.setAttr( (itemsShape[0] + '.overrideRGBColors'), 1 )
        mc.setAttr( (itemsShape[0] + '.overrideColorRGB'), self.colorR, self.colorG, self.colorB )
        #rename shape
        mc.rename(itemsShape[0], self.name + 'Shape' )

        # grp nurbs curve control
        curveGroup_offset = mc.group( em=True, n=(self.name + '_grp_offset') )
        mc.parent(nurbsCurve, curveGroup_offset)

        curveGroup = mc.group( em=True, n=(self.name + '_grp') )
        mc.parent(curveGroup_offset, curveGroup)

        # return name of control and its grp
        return curveGroup, nurbsCurve


        

    
        