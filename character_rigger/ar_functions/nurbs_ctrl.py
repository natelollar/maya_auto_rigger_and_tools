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
        #curve point positions
        nurbsCurve = mc.curve( n=(self.name), d=1, p=[  (-1, 1, 1), 
                                                        (-1, 1, -1), 
                                                        (1, 1, -1), 
                                                        (1, 1, 1), 
                                                        (-1, 1, 1), 
                                                        (-1, -1, 1), 
                                                        (-1, -1, -1), 
                                                        (1, -1, -1), 
                                                        (1, -1, 1), 
                                                        (-1, -1, 1), 
                                                        (-1, 1, 1), 
                                                        (1, 1, 1), 
                                                        (1, -1, 1), 
                                                        (1, -1, -1), 
                                                        (1, 1, -1), 
                                                        (-1, 1, -1), 
                                                        (-1, -1, -1)
                                                        ])
        #adjust scale
        mc.setAttr( (nurbsCurve + '.scale'), self.size, self.size, self.size )
        # freeze transforms
        mc.makeIdentity(apply=True)

        #access nurbs curve shape
        itemsShape = mc.listRelatives(s=True)
        mc.setAttr( (itemsShape[0] + '.overrideEnabled'), 1 )
        mc.setAttr( (itemsShape[0] + '.overrideRGBColors'), 1 )
        mc.setAttr( (itemsShape[0] + '.overrideColorRGB'), self.colorR, self.colorG, self.colorB )
        #rename shape
        mc.rename(itemsShape[0], nurbsCurve + 'Shape' )

        # grp nurbs curve control
        curveGroup_offset = mc.group( em=True, n=(nurbsCurve + '_grp_offset') )
        mc.parent(nurbsCurve, curveGroup_offset)

        curveGroup = mc.group( em=True, n=(nurbsCurve + '_grp') )
        mc.parent(curveGroup_offset, curveGroup)

        # return name of control and its grp
        return curveGroup, nurbsCurve


    def circle_ctrl( self, normal = [1,0,0] ):
        # create and name nurbs curve
        nurbsCurve_circle = mc.circle( n=(self.name), ch=False, r=10, nr=normal )
        nurbsCurve = nurbsCurve_circle[0]
        mc.setAttr( (nurbsCurve + '.scale'), self.size, self.size, self.size )
        mc.makeIdentity(apply=True)
        itemsShape = mc.listRelatives(s=True)
        mc.setAttr( (itemsShape[0] + '.overrideEnabled'), 1 )
        mc.setAttr( (itemsShape[0] + '.overrideRGBColors'), 1 )
        mc.setAttr( (itemsShape[0] + '.overrideColorRGB'), self.colorR, self.colorG, self.colorB )

        # grp nurbs curve control
        curveGroup_offset = mc.group( em=True, n=(nurbsCurve + '_grp_offset') )
        mc.parent(nurbsCurve, curveGroup_offset)

        curveGroup = mc.group( em=True, n=(nurbsCurve + '_grp') )
        mc.parent(curveGroup_offset, curveGroup)

        # return name of control and its grp
        return curveGroup, nurbsCurve

    def nurbs_sphere_ctrl( self, mat_name ):
        # create and name nurbs curve
        nurbsSphere_var = mc.sphere( n=(self.name), axis=[0,1,0], radius=1, ch=False)
        # get string of sphere name
        nurbsSphere = nurbsSphere_var[0]
        #adjust size
        mc.setAttr( (nurbsSphere + '.scale'), self.size, self.size, self.size )
        #freeze transforms
        mc.makeIdentity(apply=True)
        # color shape
        itemsShape = mc.listRelatives(s=True)
        mc.setAttr( (itemsShape[0] + '.overrideEnabled'), 1 )
        mc.setAttr( (itemsShape[0] + '.overrideRGBColors'), 1 )
        mc.setAttr( (itemsShape[0] + '.overrideColorRGB'), self.colorR, self.colorG, self.colorB )
        #creat blinn and assign blinn
        if mc.objExists(mat_name):
            mc.select(nurbsSphere)
            mc.hyperShade(assign = mat_name)
        else:
            mc.shadingNode('blinn', asShader=True, n=(mat_name))
            mc.setAttr((mat_name + '.color'), self.colorR, self.colorG, self.colorB, type='double3')
            mc.select(nurbsSphere)
            mc.hyperShade(assign = mat_name)
        # grp nurbs sphere to offset grp
        sphereGroup_offset = mc.group( em=True, n=(nurbsSphere + '_grp_offset') )
        mc.parent(nurbsSphere, sphereGroup_offset)
        # grp nurbs sphere to main grp
        sphereGroup = mc.group( em=True, n=(nurbsSphere + '_grp') )
        mc.parent(sphereGroup_offset, sphereGroup)
        # return grp and control name
        return sphereGroup, nurbsSphere


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
        mc.rename(itemsShape[0], nurbsCurve + 'Shape' )

        # grp nurbs curve control
        curveGroup_offset = mc.group( em=True, n=(nurbsCurve + '_grp_offset') )
        mc.parent(nurbsCurve, curveGroup_offset)

        curveGroup = mc.group( em=True, n=(nurbsCurve + '_grp') )
        mc.parent(curveGroup_offset, curveGroup)

        # return name of control and its grp
        return curveGroup, nurbsCurve


    def pyramid_ctrl(self):
        #curve point positions
        nurbsCurve = mc.curve( n=(self.name), d=1, p=[  (0, 5, -5), 
                                                        (-5, 0, -5), 
                                                        (0, -5, -5),
                                                        (5, 0, -5),
                                                        (0, 5, -5), 
                                                        (0, 0, 5), 
                                                        (5, 0, -5), 
                                                        (0, -5, -5), 
                                                        (0, 0, 5), 
                                                        (-5, 0, -5), 
                                                        ])
        #adjust scale
        mc.setAttr( (nurbsCurve + '.scale'), self.size, self.size, self.size )
        # freeze transforms
        mc.makeIdentity(apply=True)

        #access nurbs curve shape
        itemsShape = mc.listRelatives(s=True)
        mc.setAttr( (itemsShape[0] + '.overrideEnabled'), 1 )
        mc.setAttr( (itemsShape[0] + '.overrideRGBColors'), 1 )
        mc.setAttr( (itemsShape[0] + '.overrideColorRGB'), self.colorR, self.colorG, self.colorB )
        #rename shape
        mc.rename(itemsShape[0], nurbsCurve + 'Shape' )

        #renaming curve inturn renames all its shapes
        nurbsCurve_name = mc.rename(nurbsCurve, nurbsCurve + '#')

        # grp nurbs curve control
        curveGroup_offset = mc.group( em=True, n=(nurbsCurve_name + '_grp_offset') )
        mc.parent(nurbsCurve_name, curveGroup_offset)

        curveGroup = mc.group( em=True, n=(nurbsCurve_name + '_grp') )
        mc.parent(curveGroup_offset, curveGroup)

        # return name of control and its grp
        return curveGroup, nurbsCurve_name

    
    def sphere_ctrl(self):
        #create nurbs circle
        curveA_circle = mc.circle( n=self.name, ch=False, r=3, nr=(0,1,0))
        curveA = curveA_circle[0]
        #create variable for nurbs circle shape
        mc.listRelatives(curveA, s=True)
        #color nurbs circle shape
        mc.setAttr( ('.overrideEnabled'), 1 )
        mc.setAttr( ('.overrideRGBColors'), 1 )
        mc.setAttr( ('.overrideColorRGB'), self.colorR, self.colorG, self.colorB )
        #adjust scale
        mc.setAttr( ('.scale'), self.size, self.size, self.size )
        # freeze transforms
        mc.makeIdentity(apply=True)
        
        #create 2nd nurbs circle
        curveB_circle = mc.circle(ch=False, r=3, nr=(0,0,0))
        curveB = curveB_circle[0]
        #create variable for 2nd nurbs circle shape
        curveB_circle_shape = mc.listRelatives(curveB, s=True)
        curveB_shape = curveB_circle_shape[0]
        #color 2nd nurbs circle shape
        mc.setAttr(('.overrideEnabled'), 1)
        mc.setAttr(('.overrideRGBColors'), 1)
        mc.setAttr(('.overrideColorRGB'), self.colorR, self.colorG, self.colorB )
        #adjust scale
        mc.setAttr( ('.scale'), self.size, self.size, self.size )
        # freeze transforms
        mc.makeIdentity(apply=True)
        #parent shape to main transform
        mc.parent(curveB_shape, curveA, r=True, shape=True)
        #delete 2nd nurbs circle transform
        mc.delete(curveB)
        
        #create 3rd nurbs circle
        curveC_circle = mc.circle(ch=False, r=3, nr=(1,0,0))
        curveC = curveC_circle[0]
        #create variable for 3rd nurbs circle shape
        curveC_circle_shape = mc.listRelatives(curveC, s=True)
        curveC_shape = curveC_circle_shape[0]
        #color 3rd nurbs circle shape
        mc.setAttr((".overrideEnabled"), 1)
        mc.setAttr((".overrideRGBColors"), 1)
        mc.setAttr(('.overrideColorRGB'), self.colorR, self.colorG, self.colorB )
        #adjust scale
        mc.setAttr( ('.scale'), self.size, self.size, self.size )
        # freeze transforms
        mc.makeIdentity(apply=True)
        #parent shape to main transform
        mc.parent(curveC_shape, curveA, r=True, shape=True)
        #delete 3rd nurbs circle transform
        mc.delete(curveC)
        
        #rename shapes
        shapeList = mc.listRelatives(curveA, s=True)
        mc.rename(shapeList[1], self.name + 'AShape' )
        mc.rename(shapeList[2], self.name + 'BShape' )

        #renaming curve inturn renames all its shapes
        curveA_name = mc.rename(curveA, curveA + '#')

        # grp nurbs curve control
        curveGroup_offset = mc.group( em=True, n=(curveA_name + '_grp_offset') )
        mc.parent(curveA_name, curveGroup_offset)

        curveGroup = mc.group( em=True, n=(curveA_name + '_grp') )
        mc.parent(curveGroup_offset, curveGroup)

        # return name of control and its grp
        return curveGroup, curveA_name


    def tri_circle_ctrl(self):
        #create nurbs circle
        curveA_circle = mc.circle( n=self.name, ch=False, r=3, nr=(0,1,0))
        curveA = curveA_circle[0]
        #create variable for nurbs circle shape
        curveA_shape = mc.listRelatives(curveA, s=True)
        #color nurbs circle shape
        mc.setAttr( ('.overrideEnabled'), 1 )
        mc.setAttr( ('.overrideRGBColors'), 1 )
        mc.setAttr( ('.overrideColorRGB'), self.colorR, self.colorG, self.colorB )
        #adjust scale
        mc.setAttr( ('.scale'), self.size, self.size, self.size )
        # freeze transforms
        mc.makeIdentity(apply=True)

        #create 2nd nurbs circle
        curveB_circle = mc.circle( n=curveA[0] + 'A', ch=False, r=3, nr=(0,1,0))
        curveB = curveB_circle[0]
        mc.move(0, 5, 0, r=True )
        #create variable for 2nd nurbs circle shape
        curveB_circle_shape = mc.listRelatives(curveB, s=True)
        curveB_shape = curveB_circle_shape[0]
        #color 2nd nurbs circle shape
        mc.setAttr(('.overrideEnabled'), 1)
        mc.setAttr(('.overrideRGBColors'), 1)
        mc.setAttr(('.overrideColorRGB'), self.colorR, self.colorG, self.colorB )
        #adjust scale
        mc.setAttr( ('.scale'), self.size, self.size, self.size )
        # freeze transforms
        mc.makeIdentity(apply=True)
        #parent 2nd nurbs circle shape to first nurbs circle
        mc.parent(curveB_shape, curveA, r=True, shape=True)
        #delete 2nd nurbs circle transform
        mc.delete(curveB)

        #create 3rd nurbs circle
        curveC_circle = mc.circle( n=curveA[0] + 'B', ch=False, r=3, nr=(0,1,0))
        curveC = curveC_circle[0]
        mc.move(0, -5, 0, r=True )
        #create variable for 3rd nurbs circle shape
        curveC_circle_shape = mc.listRelatives(curveC, s=True)
        curveC_shape = curveC_circle_shape[0]
        #color 3rd nurbs circle shape
        mc.setAttr(('.overrideEnabled'), 1)
        mc.setAttr(('.overrideRGBColors'), 1)
        mc.setAttr(('.overrideColorRGB'), self.colorR, self.colorG, self.colorB )
        #adjust scale
        mc.setAttr( ('.scale'), self.size, self.size, self.size )
        # freeze transforms
        mc.makeIdentity(apply=True)
        #parent 3rd nurbs circle shape to first nurbs circle
        mc.parent(curveC_shape, curveA, r=True, shape=True)
        #delete 3rd nurbs circle transform
        mc.delete(curveC)

        #scale to reshape points
        mc.scale(2.5, 1, 2.5, curveA, r=True)
        mc.makeIdentity(curveA, apply=True)

        #rename shapes
        shapeList = mc.listRelatives(curveA, s=True)
        mc.rename(shapeList[1], self.name + 'AShape' )
        mc.rename(shapeList[2], self.name + 'BShape' )

        #renaming curve inturn renames all its shapes
        curveA_name = mc.rename(curveA, curveA + '#')

        # grp nurbs curve control
        curveGroup_offset = mc.group( em=True, n=(curveA_name + '_grp_offset') )
        mc.parent(curveA_name, curveGroup_offset)

        curveGroup = mc.group( em=True, n=(curveA_name + '_grp') )
        mc.parent(curveGroup_offset, curveGroup)

        # return name of control and its grp
        return curveGroup, curveA_name
    

    def locator_ctrl(self):
        #curve point positions
        nurbsCurve = mc.curve( n=(self.name), d=1, p=[  (0.0, 0.0, 5.0),
                                                        (0.0, 0.0, -5.0),
                                                        (0.0, 0.0, 0.0),
                                                        (-5.0, 0.0, 0.0),
                                                        (5.0, 0.0, 0.0),
                                                        (0.0, 0.0, 0.0),
                                                        (0.0, 5.0, 0.0),
                                                        (0.0, 0.0, 0.0),
                                                        (0.0, -5.0, 0.0) 
                                                        ])
        #adjust scale
        mc.setAttr( (nurbsCurve + '.scale'), self.size, self.size, self.size )
        # freeze transforms
        mc.makeIdentity(apply=True)

        #access nurbs curve shape
        itemsShape = mc.listRelatives(s=True)
        mc.setAttr( (itemsShape[0] + '.overrideEnabled'), 1 )
        mc.setAttr( (itemsShape[0] + '.overrideRGBColors'), 1 )
        mc.setAttr( (itemsShape[0] + '.overrideColorRGB'), self.colorR, self.colorG, self.colorB )
        #rename shape
        mc.rename(itemsShape[0], nurbsCurve + 'Shape' )

        # grp nurbs curve control
        curveGroup_offset = mc.group( em=True, n=(nurbsCurve + '_grp_offset') )
        mc.parent(nurbsCurve, curveGroup_offset)

        curveGroup = mc.group( em=True, n=(nurbsCurve + '_grp') )
        mc.parent(curveGroup_offset, curveGroup)

        # return name of control and its grp
        return curveGroup, nurbsCurve


        

    
        