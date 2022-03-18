## Nate Tools Character Rigger Toolset ReadMe...<br/>
> Mainly Tested in Maya 2020.4, Windows 10, Python 2.7.11 (though, should work in Maya 2022 and 2019)

First, place the 'character_rigger' folder in root level of the Maya scripts folder.   
> C:\Users\Bob\Documents\maya\2020\scripts
  
( or add path to maya.env as PYTHONPATH = ' ' )     

*'ar' stands for 'auto rig'*  
*launch 'rigger_ui.py' in 'ar_ui' folder*  

Launch the UI with this Python code:
```bash
import character_rigger
character_rigger.ar_ui.rigger_ui.rigger_ui_class().rigger_ui_method()
```

*make a shelf button by middle mouse dragging this code to a Maya shelf from the script editor*  
    (the launch script is also in the 'launch_ui.py' file)  
    (shelf button icon is in 'character_rigger < icons' folder)  

*if Maya has trouble importing files, use the 'import_reload.py' file to import and reload all files*  
    ( consider making a shelf button of this too ) 



## *'Auto Rig' Tab Notes*  
>Limitations and How-to

1. No joint names or selections are needed.  The auto rigger automatically finds all the joints<br/> 
and rigs the skeleton when RIG ME! is clicked.<br/>

2. Mid Face Jnts selects the lowest top face joints in the Y position.<br/>
Mid Face Jnts constrains the joints halfway between the head and the jaw, opposed to just the head.<br/>

3. The forearm twist chain should be considered seperate and only parented to the elbow.<br/>
In other words, the wrist should be parented to the elbow and not the twist joints.<br/>
Nothing should be parented to the end of the twist chain for the current setup.<br/>

4. The foot locators are not required but will give the reverse foot pivots exact positions instead of the preset.<br/>

5. Currently the 'head joints' require top face jnts parented to the head, a jaw jnt parented to the head jnt,<br/> 
bottom face jnts parented to the jaw, and a tongue jnt chain parented to the jaw jnt.<br/> 
Ears are considered top face jnts with a child/s jnt and there would be two ears, but they are not required.<br/>
(The head and top neck joint refer to the same joint.)<br/>

6. Uncheck 'Head Jnts' if there are no before mentioned head joints and only a top neck joint. Or if the head controls are not needed.<br/>

7. There is currently only a forearm twist.  The single twist joint or chain should be parented to the elbow and nothing parented to it.<br/>
Uncheck the 'Forearm Twst Jnts' if the character has no forearm twist joints.<br/>

8. The Elbow and Knee 'PV Dist' text field sets the preset distance the IK elbow and knee ctrls are away from the elbows and knees.<br/>
This can be changed after auto rigging by translating the parent grp of each control on its main axis.<br/>

9. Currently the main axis for the rig is X down the chain and Y pointing outwards.<br/>
This is Y up on the arms and fingers, and Y forward on the legs, spine and neck.<br/>
If X is not directly down the chain, the IK elbows and knees may move unwantingly on rig creation.<br/>

10. Currently, the ankle and toe jnt should be level with the ground, so that the ankle and toe ctrls are not at a downward angle.<br/>
Otherwise x down the chain like the other jnts.<br/>

11. However, the 'head joints' aside from the tongue can be oriented to the default world position.<br/>

12. It should be noted that the right arm and leg are mirriored across YZ with the mirror function set to 'Behavior'<br/>
with the 'Skeleton < Mirror Joints' setting.  The same as multiplying the translate x,y,z * (-1,1,1) and rotation x,y,z * (1,-1,-1)<br/>
and then substracting 180 degrees from the rotate X. This should be noted if mirroring reverse foot locators across X axis.<br/>

13. XYZ is currently the rotation order for all the joints.<br/>   

14. Note there should be a bend in the elbow and knees of the skeleton.<br/>

15. There is no real limit on the spine, neck or finger jnt chain length.<br/>

16. The rig is made at Maya's default distance scale, where 1 unit = 1 cm. A 6ft human would be 182.88 maya units (cm) tall.<br/>
In other words the same as Unreal Engine. And also the size of the humanBody base sculpt mesh in the Maya 'content browser'.<br/>

17. The rig supports global scaling and uniform scaling of most all individual joints. Non-uniform joint scaling is not currently supported.<br/>

18. Check the included skeleton in the 'other' folder to see a possible joint setup.<br/>

19. Finally, export skin weights with 'Deform < Export Weights...' as an .xml to use with the 'New Skinned Character Scene' button.<br/>
The button automatically creates a new scene and skins the selected skeleton to the selected mesh with the xml weights.<br/>
First all weight is automatically applied to the root joint, and then skin weights applied, to avoid errors.<br/>
And make sure the fbxmaya.dll plugin is loaded into Maya if importing fbx files for the body or skeleton.<br/>


## 'Rigging' Tab Notes  
>Limitations and How-to

For the rigging tab the functions are, FK chain creation, IK limb creation, FK IK blended chain creation, 
auto creating a blend color node blend, automatically creating FK IK joint chains connected with blend color nodes to a main joint chain, 
creating a reverse foot setup based on locator positions, and creating several nurbs curve controls.   

In addition, there is a button to create a new bind pose for a skeleton while deleting the old bindpose.

Also, the 'Print Object Type' button prints the type of the selected object in the script editor.

The 'Mirror Ctrl Shapes' button allows a rigger to easily mirror the shapes of controls across the X axis without having to 
tediously match them manually or through some other means.


**_____'Animation' Tab Notes_____**
*limitations and How-to*

The animation tab includes a multi-parent constraint for moving multiple controls in worldspace.  
One would key the controls after they were moved and delete the locator they are parented to, auto deleting the constraints.  
This allows a full character to be rotated in world space.  

In addition there is a function to mirror left control attributes to the right side.   
This would be useful if one was creating set driven keys for a hand and needed to easily copy the poses to the right hand.  
Also, if no opposite controls exist, the mirror control function will instead mirror the selected control to the other side.   


**_____'Modeling' Tab Notes_____**  
*limitations and How-to*  

1. For the modeling tab there is a function to create random objects for testing.    

2. Also, there is the ability to scatter objects randomly anywhere within a radius or to the verts of another object.     

3. In addition, the modeling tab has a button to import the default human sculpt model in Maya and also to create a polygon arch from code.  

4. Finally, the modeling tab has a button to export multiple objects at once to individual .obj, .fbx, or .ma files.    
This is useful because Maya does not have a multi export built in for '.obj'.  


**_____'Color' Tab Notes_____**
*limitations and How-to*

The color tab has the ability to change the color of shapes, transforms, and the wire color of shapes and transforms.  
There is also the option to change the outliner color of an object.  
These functions can be used to change joint color, control curve color, or the wireframe color of an object.
An option to change the thickness of a curve has also been added.


**_____'Misc' Tab Notes_____**
*limitations and How-to*

The miscellaneous tab has extra functions that have not been organized into the other tabs yet, 
or that don't belong in one of the categories.

The Maya and Python version can be printed out in the script editor console.  There is a button to add a test function.
And a funciton to print out the positions of the vertices in a curve, including multiple shapes in a curve.

An option to change the display type of a curve to 'reference,' for instance, to avoid selection of a global control during animation.
Next to that is the option to rename the first occurence of a string, in a name, to something.

Also, there is a button to constrain a group of objects between the last two selected objects.  

An option to scale constrain an object to multiple objects at once, not possible in default Maya.

One can set the numerical value of an objects attribute name as well.

Finally, there is an option to automatically set up Set Driven Keys to multiple objects with 1 contraint per object, 
tied to a switch control attribute.



**_____Other Notes and Thoughts_____**
**___________________________________**

In the future bounding box selection may be implemented to the auto rigger for a hybrid approach.
It seams finding the joints via other joints, for instance, the root joint being the joint with the most children in the scene,
lacks some flexibility for modularity.  If one would want 5 arms coming out of a toe, this becomes unnecessarily complicated
to look at all the other joints around when one could just place a bounding box selector at the root of each appendage instead.
I think placing bounding box selectors, where joints may be unpredictable, like the face, would be a good hybrid approach. 
In addition to finding joints based on other joints and based on bounding boxes; world position, vectors based on other joints, 
or joint labels could also be used.  This all allows the rig to operate without joint names making it more flexible and easier to use,
not requring selecting joints or typing in names, both repetitive tasks.

Though, a fully modular setup may be better for the auto rigger, where placing stand-in objects would represent joints and
then joint orientation could be better accounted for.  It is nice to be able to use an auto rigger on a pre-existing skeleton,
but this could be managed by having an easy way to import skin weights onto the new skeleton from an old weighted skeleton.

Snappable knees and elbows need to be added.  Possibly bendy limbs could be combined with this addition.  I like the full scalability
of all the limbs, and joints including twist joints but I wonder if this adds unnecessary complication to worry about scaling all the rig functions individually.
And how often do individual joints need to be scaled unless for a cartoony character.  Though global character scale is more important.

A spline IK spine option may be added.  Auto clavicle/ scapula could also be included.

Possibly premade set driven keys for the fingers and face ctrls.  For basic facial and hand expresions like fingers spread and fist.

It would be neat to add a rag doll checkbox to the rig.  I made one with bullet physics that could move with the rig.  
However, bullet physics seams clunky and possibly nCloth might be a better route for ragdoll.

I hope to add a pose saver to the rigging toolset.

The python scripts could be better organized.  Better use of classes could also be made to reduce repeating code.

Finally, I would like to dig into the Maya API as well to add some interesting functionality to the Character Rigger Toolset.

**___________________________________**

The toolset has been mainly test in Maya 2020 Python 2.7, but has also been tested in Python 3 for Maya 2022.


