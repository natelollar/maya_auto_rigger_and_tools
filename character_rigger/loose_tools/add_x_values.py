import maya.cmds as mc

mySel = mc.ls(sl=1)

x_val_total = 0
for i in mySel:
    x_val = mc.getAttr(i + '.tx')
    print(x_val)
    x_val_total += x_val
    
print(x_val_total)




