# On Robot Computer

1) Place robot over object that is going to be added.

2) Run the position_finder.py file which is in the User_Study_Object_Placement directory.

3) Put the x and y position into transform_obj.py file and make sure to add new object to the object array.


# On Unity computer

1) In SpawnObjects.cs (placed on objects game object), if the number of objects is being changed, make sure to add new public Gameobject Object Prefab near line 24.

2) Add in the hardcoded colour for this object in the objColors array.

3) Update prefabArray on line 40

4) Drag and drop prefab to object filed in objects gameobject.