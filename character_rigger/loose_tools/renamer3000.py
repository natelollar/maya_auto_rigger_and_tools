from maya import cmds

my_sel = cmds.ls(selection=True)
rename01 = True
prefix01 = False
to_replace01 = "r_"
replace01 = "l_"
#to_replace02 = "_geo_"
#replace02 = "_"
prefix_string = "r_"
my_sel = cmds.ls(selection=True)
if rename01 == True:
    for object in my_sel:
        object_base_name = object.split('|')[-1]
        object_new_name = object_base_name.replace(to_replace01, replace01)
        cmds.rename(object, object_new_name)
        #print(object_name)
# else:
#     for object in my_sel:
#         object = str(object)
#         object_name = object.replace(to_replace02, replace02)
#         cmds.rename(object, object_name)
# if prefix01 == True:
#     for object in my_sel:
#         object = str(object)
#         object_name = prefix_string + object
#         cmds.rename(object, object_name)
