import maya.cmds as mc

def four_arrow_ctrl():

    myCurve0 = mc.curve(p=[ 
                        (-71.438, 0.0, -71.438),
                        (-57.509, 0.0, -84.796),
                        (-41.145, 0.0, -92.642),
                        (-26.517, 0.0, -97.227),
                        (-26.517, 0.0, -97.227),
                        (-26.517, 0.0, -97.227),
                        (-24.436, 0.0, -118.027),
                        (-24.436, 0.0, -118.027),
                        (-24.436, 0.0, -118.027),
                        (-48.922, 0.0, -117.978),
                        (-48.922, 0.0, -117.978),
                        (-48.922, 0.0, -117.978),
                        (0.0, 0.0, -205.925),
                        (0.0, 0.0, -205.925),
                        (0.0, 0.0, -205.925),
                        (49.02, 0.0, -118.175),
                        (49.02, 0.0, -118.175),
                        (49.02, 0.0, -118.175),
                        (24.535, 0.0, -118.126),
                        (24.535, 0.0, -118.126),
                        (24.535, 0.0, -118.126),
                        (26.517, 0.0, -97.227),
                        (26.517, 0.0, -97.227),
                        (26.517, 0.0, -97.227),
                        (42.538, 0.0, -91.659),
                        (58.975, 0.0, -83.918),
                        (71.438, 0.0, -71.438)
                        ] )

    myCurve1 = mc.duplicate(myCurve0)
    mc.setAttr(myCurve1[0] + '.scaleZ', -1)
    mc.makeIdentity(myCurve1, apply=True)

    myCurve2 = mc.duplicate(myCurve0)
    mc.setAttr(myCurve2[0] + '.rotateY', -90)
    mc.makeIdentity(myCurve2, apply=True)

    myCurve3 = mc.duplicate(myCurve0)
    mc.setAttr(myCurve3[0] + '.rotateY', 90)
    mc.makeIdentity(myCurve3, apply=True)

    myCurveCircle = mc.circle(r=93, nr=(0,1,0), ch=0)


    crv_lst = [myCurve0, myCurve1, myCurve2, myCurve3, myCurveCircle]

    crvShp_lst = []
    for i in crv_lst:
        crv_shp = mc.listRelatives(i, s=True)
        mc.setAttr((crv_shp[0] + '.overrideEnabled'), 1)
        mc.setAttr((crv_shp[0] + '.overrideRGBColors'), 1)
        mc.setAttr((crv_shp[0] + '.overrideColorRGB'), .1, .8, 0)
        mc.setAttr((crv_shp[0] + '.lineWidth'), 1.5)

        
        crvShp_lst.append(crv_shp)


    for i in crvShp_lst[1:]:
        mc.parent(i, myCurve0, r=1, s=1)

    for i in crv_lst[1:]:
        mc.delete(i) # delete empty transforms
        
    for i in crvShp_lst:
        mc.rename(i, 'fourArrow_ctrlShape#') # to make sure all shapes get renamed # glitch with circle shape
        
    mc.rename(myCurve0, 'fourArrow_ctrl#')

    mc.select(cl=True)





