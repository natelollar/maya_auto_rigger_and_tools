import maya.cmds as mc

class create_jnts():

    def __init__(self, name, size, colorR, colorG, colorB):
        self.name = name
        self.size = size
        self.colorR = colorR
        self.colorG = colorG
        self.colorB = colorB

    def single_jnt(self):
        myJoint = mc.joint( n = self.name )
        #size and color
        mc.setAttr('.radius', self.size)
        mc.setAttr('.overrideEnabled', 1)
        mc.setAttr('.overrideRGBColors', 1)
        mc.setAttr('.overrideColorRGB', self.colorR, self.colorG, self.colorB)
        #turn off scale compensate to prevent double scaling (when global scaling)
        mc.setAttr('.segmentScaleCompensate', 0 )

        return myJoint
