#This program reads all the meshes in a Blender Scene to Convert it into a Graph to construct a wireframe before we can remodel the entire mesh in PySoy
#Graph is saved into a file named "mesh_details.txt" in the Blender folder from which you ran Blender

import bpy

g_scene=[]
for mesh in bpy.data.meshes:
    g_mesh=[]
    for i in range(len(mesh.vertices)):
        g_mesh.append([])
    for edge in mesh.edges:
        g_mesh[mesh.vertices[edge.vertices[0]].index].append(mesh.vertices[edge.vertices[1]].index)
        g_mesh[mesh.vertices[edge.vertices[1]].index].append(mesh.vertices[edge.vertices[0]].index)
    g_scene.append(g_mesh)
             
print(g_scene)

f=open("mesh_details.txt",'w')
for mesh in g_scene:
    for vert in mesh:
        for i in range(len(vert)):
            f.write(str(vert[i])+' ')
        f.write('\n')
    f.write('\n')
f.close()
