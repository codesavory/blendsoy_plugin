To run the python script for Blender which converts blender data to Pysoy

Steps to follow for Setup:
1. Download Blender tarball from: http://www.blender.org/download/ (Note that the work was tested in Blenderv2.74.0, unless blender has drastically changed you must be able to run it on any latest Blender)
2. Extract it using either any Archive Manager or run cmd:
$tar xvjf filename.tar.bz2
3. Open Terminal, go to this folder location you just extracted, run cmd: 
$./blender
4. You will now be running Blender, you can have fun with it here.
Note: To run the PySoy scripts below, you will have to copy the pysoy module "soy.cpython-34m.so" from python packages location: '$/usr/lib/python3.*' or '$/usr/lib/python3.*/dist-packages' to your blender folder you extracted initially: '$/yourblenderpath/2.*/scripts/modules'.
*: Represents the version of python and blender you have downloaded or installed in your system.

Steps to run the script:
1. Change the Blender screen to 'Scripting' on the top tool bar.
2. In the Text Editor window, click 'open a new text block' button to the right.
3. Go to the location of the script 'pysoy_modeller.py' in this same directory and click open text block.
4. Click 'Run Script' to convert it to PySoy code.

Files:
1. basic_modeling_script.py:
This was the basic work, where basic shapes in Blender could be read and this would be converted to the corresponding shape in PySoy. Basically, redundant now.
2. edge_wireframe_generate.py:
This is text file generator, which reads a mesh in the Blender scene and generates the edge graph, also called wireframe i.e., it identifies to which other vertices each vertex is connected via that edge.
3. face_surface_generate.py:
This is another generative file, which reads a mesh in Blender scene and generates the surface i.e., it reads all the faces of the mesh and finds out which all vertices are used to create each surface.
4. mesh_vertices_generate.py:
This is another generative file, which lists all the vertices of a mesh.
5. pysoy_modeller.py:
This is the main file, which combines all the above generator file to model the Blender mesh in PySoy. You can see the Blender Scene being converted to PySoy Scene. Though it works, there are still lots of bugs to be fixed.
Warning: Blender might crash running the above scripts. Use with caution, though you can just run it again. Nothing to worry.
