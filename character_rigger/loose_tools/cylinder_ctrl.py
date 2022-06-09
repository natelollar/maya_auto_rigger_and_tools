import maya.cmds as mc

class cylinder_ctrl():

    def cylinder_ctrl_hard(self):   
        print('cylinder_ctrl_hard!')
        #___________________________________________________________________
        myCurve0 = mc.curve( degree=1, p=[ 
                                (21.213, 25.0, -21.213),
                                (0.0, 25.0, -30.0),
                                (-21.213, 25.0, -21.213),
                                (-30.0, 25.0, 0.0),
                                (-21.213, 25.0, 21.213),
                                (0.0, 25.0, 30.0),
                                (21.213, 25.0, 21.213),
                                (30.0, 25.0, 0.0),
                                (30.0, 25.0, 0.0)
                            ] )

        myCurve0 = mc.closeCurve(   myCurve0, 
                                    constructionHistory=False, 
                                    preserveShape=1, # 0 - without preserving the shape 1 - preserve shape 2 - blend
                                    replaceOriginal=True, 
                                    blendBias=0.5, 
                                    blendKnotInsertion=False, 
                                    parameter=0.1)

        
        #___________________________________________________________________
        myCurve1 = mc.curve(degree=1,p=[
                            (-21.213, 25.0, 21.213),
                            (-21.213, 0.0, 21.213),
                            (-21.213, -25.0, 21.213),
                            ] )
        #___________________________________________________________________
        myCurve2 = mc.curve(degree=1,p=[
                            (-30.0, 25.0, 0.0),
                            (-30.0, 0.0, 0.0),
                            (-30.0, -25.0, 0.0),
                            ] )
        #___________________________________________________________________
        myCurve3 = mc.curve(degree=1,p=[
                            (-21.213, 25.0, -21.213),
                            (-21.213, 0.0, -21.213),
                            (-21.213, -25.0, -21.213),
                            ] )
        #___________________________________________________________________
        myCurve4 = mc.curve(degree=1,p=[
                            (0.0, 25.0, -30.0),
                            (0.0, 0.0, -30.0),
                            (0.0, -25.0, -30.0),
                            ] )
        #___________________________________________________________________
        myCurve5 = mc.curve(degree=1,p=[
                            (21.213, 25.0, -21.213),
                            (21.213, 0.0, -21.213),
                            (21.213, -25.0, -21.213),
                            ] )
        #___________________________________________________________________
        myCurve6 = mc.curve(degree=1,p=[
                            (30.0, 25.0, 0.0),
                            (30.0, 0.0, 0.0),
                            (30.0, -25.0, 0.0),
                            ] )
        #___________________________________________________________________
        myCurve7 = mc.curve(degree=1,p=[
                            (21.213, 25.0, 21.213),
                            (21.213, 0.0, 21.213),
                            (21.213, -25.0, 21.213),
                            ] )
        #___________________________________________________________________
        myCurve8 = mc.curve(degree=1,p=[
                            (0.0, 25.0, 30.0),
                            (0.0, 0.0, 30.0),
                            (0.0, -25.0, 30.0),
                            ] )
        #___________________________________________________________________
        myCurve9 = mc.curve(degree=1,p=[
                            (21.213, -25.0, -21.213),
                            (0.0, -25.0, -30.0),
                            (-21.213, -25.0, -21.213),
                            (-30.0, -25.0, 0.0),
                            (-21.213, -25.0, 21.213),
                            (0.0, -25.0, 30.0),
                            (21.213, -25.0, 21.213),
                            (30.0, -25.0, 0.0),
                            (30.0, -25.0, 0.0),
                            ] )
        
        myCurve9 = mc.closeCurve(   myCurve9, 
                                    constructionHistory=False, 
                                    preserveShape=1, # 0 - without preserving the shape 1 - preserve shape 2 - blend
                                    replaceOriginal=True, 
                                    blendBias=0.5, 
                                    blendKnotInsertion=False, 
                                    parameter=0.1)
        
        #___________________________________________________________________
        myCurve10 = mc.curve(degree=1,p=[
                            (21.213, 0.0, -21.213),
                            (0.0, 0.0, -30.0),
                            (-21.213, 0.0, -21.213),
                            (-30.0, 0.0, 0.0),
                            (-21.213, 0.0, 21.213),
                            (0.0, 0.0, 30.0),
                            (21.213, 0.0, 21.213),
                            (30.0, 0.0, 0.0),
                            (30.0, 0.0, 0.0),
                            ] )
        
        myCurve10 = mc.closeCurve(   myCurve10, 
                                    constructionHistory=False, 
                                    preserveShape=1, # 0 - without preserving the shape 1 - preserve shape 2 - blend
                                    replaceOriginal=True, 
                                    blendBias=0.5, 
                                    blendKnotInsertion=False, 
                                    parameter=0.1)
        
        #___________________________________________________________________

        curve_list = [ #myCurve0,
                    myCurve1,
                    myCurve2,
                    myCurve3,
                    myCurve4,
                    myCurve5,
                    myCurve6,
                    myCurve7,
                    myCurve8,
                    myCurve9,
                    myCurve10
                    ]

        for i in curve_list:

            shp = mc.listRelatives(i, shapes=True)

            mc.parent( shp, myCurve0, relative=True, shape=True)

            # delete extra transforms
            mc.delete(i)

        myCurve0_name = mc.rename(myCurve0, 'cylinder_ctrl#')

        shp_new = mc.listRelatives(myCurve0_name, shapes=True)
        print(shp_new)
        for i in shp_new:
            mc.rename(i, myCurve0_name + '_1')


        mc.select(cl=True)

    
    # WIP, not finished
    def cylinder_ctrl_smooth(self):   
        print('cylinder_ctrl_smooth!')
        
        #___________________________________________________________________
        
        myCurve0 = mc.curve( degree=2, p=[ 
                                (21.213, 25.0, -21.213),
                                (0.0, 25.0, -30.0),
                                (-21.213, 25.0, -21.213),
                                (-30.0, 25.0, 0.0),
                                (-21.213, 25.0, 21.213),
                                (0.0, 25.0, 30.0),
                                (21.213, 25.0, 21.213),
                                (30.0, 25.0, 0.0),
                                (30.0, 25.0, 0.0)
                            ] )
        
        myCurve0 = mc.closeCurve(   myCurve0, 
                                    constructionHistory=False, 
                                    preserveShape=1, # 0 - without preserving the shape 1 - preserve shape 2 - blend
                                    replaceOriginal=True, 
                                    blendBias=0.5, 
                                    blendKnotInsertion=False, 
                                    parameter=0.1)

        
        #___________________________________________________________________
        myCurve1 = mc.curve(degree=2,p=[
                            (-21.213, 25.0, 21.213),
                            (-21.213, 0.0, 21.213),
                            (-21.213, -25.0, 21.213),
                            ] )
        
        #___________________________________________________________________
        myCurve2 = mc.curve(degree=2,p=[
                            (-30.0, 25.0, 0.0),
                            (-30.0, 0.0, 0.0),
                            (-30.0, -25.0, 0.0),
                            ] )
        #___________________________________________________________________
        myCurve3 = mc.curve(degree=2,p=[
                            (-21.213, 25.0, -21.213),
                            (-21.213, 0.0, -21.213),
                            (-21.213, -25.0, -21.213),
                            ] )
        #___________________________________________________________________
        myCurve4 = mc.curve(degree=2,p=[
                            (0.0, 25.0, -30.0),
                            (0.0, 0.0, -30.0),
                            (0.0, -25.0, -30.0),
                            ] )
        #___________________________________________________________________
        myCurve5 = mc.curve(degree=2,p=[
                            (21.213, 25.0, -21.213),
                            (21.213, 0.0, -21.213),
                            (21.213, -25.0, -21.213),
                            ] )
        #___________________________________________________________________
        myCurve6 = mc.curve(degree=2,p=[
                            (30.0, 25.0, 0.0),
                            (30.0, 0.0, 0.0),
                            (30.0, -25.0, 0.0),
                            ] )
        #___________________________________________________________________
        myCurve7 = mc.curve(degree=2,p=[
                            (21.213, 25.0, 21.213),
                            (21.213, 0.0, 21.213),
                            (21.213, -25.0, 21.213),
                            ] )
        #___________________________________________________________________
        myCurve8 = mc.curve(degree=2,p=[
                            (0.0, 25.0, 30.0),
                            (0.0, 0.0, 30.0),
                            (0.0, -25.0, 30.0),
                            ] )
        #___________________________________________________________________
        myCurve9 = mc.curve(degree=2,p=[
                            (21.213, -25.0, -21.213),
                            (0.0, -25.0, -30.0),
                            (-21.213, -25.0, -21.213),
                            (-30.0, -25.0, 0.0),
                            (-21.213, -25.0, 21.213),
                            (0.0, -25.0, 30.0),
                            (21.213, -25.0, 21.213),
                            (30.0, -25.0, 0.0),
                            (30.0, -25.0, 0.0),
                            ] )
        
        myCurve9 = mc.closeCurve(   myCurve9, 
                                    constructionHistory=False, 
                                    preserveShape=1, # 0 - without preserving the shape 1 - preserve shape 2 - blend
                                    replaceOriginal=True, 
                                    blendBias=0.5, 
                                    blendKnotInsertion=False, 
                                    parameter=0.1)
        
        #___________________________________________________________________
        myCurve10 = mc.curve(degree=2,p=[
                            (21.213, 0.0, -21.213),
                            (0.0, 0.0, -30.0),
                            (-21.213, 0.0, -21.213),
                            (-30.0, 0.0, 0.0),
                            (-21.213, 0.0, 21.213),
                            (0.0, 0.0, 30.0),
                            (21.213, 0.0, 21.213),
                            (30.0, 0.0, 0.0),
                            (30.0, 0.0, 0.0),
                            ] )
        
        myCurve10 = mc.closeCurve(  myCurve10, 
                                    constructionHistory=False, 
                                    preserveShape=1, # 0 - without preserving the shape 1 - preserve shape 2 - blend
                                    replaceOriginal=True, 
                                    blendBias=0.5, 
                                    blendKnotInsertion=False, 
                                    parameter=0.1)
        
        #___________________________________________________________________

        curve_list = [ #myCurve0,
                    myCurve1,
                    myCurve2,
                    myCurve3,
                    myCurve4,
                    myCurve5,
                    myCurve6,
                    myCurve7,
                    myCurve8,
                    myCurve9,
                    myCurve10
                    ]

        for i in curve_list:

            shp = mc.listRelatives(i, shapes=True)

            mc.parent( shp, myCurve0, relative=True, shape=True)

            # delete extra transforms
            mc.delete(i)

        myCurve0_name = mc.rename(myCurve0, 'cylinder_ctrl#')

        shp_new = mc.listRelatives(myCurve0_name, shapes=True)
        print(shp_new)
        for i in shp_new:
            mc.rename(i, myCurve0_name + '_1')


        mc.select(cl=True)

    



#cylinder_ctrl().cylinder_ctrl_hard()
