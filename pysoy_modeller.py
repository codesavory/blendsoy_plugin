import bpy
import os
import soy
from time import sleep

#generate the face mesh file        
f=open("mesh_face_details.txt",'w')        
for mesh in bpy.data.meshes:
    print(mesh.name)
    print(len(mesh.polygons))
    f.write(mesh.name)
    f.write('\n')
    for face in mesh.polygons:
        if(len(face.vertices)==3):
            for vert in face.vertices:
                f.write(str(mesh.vertices[vert].index)+' ')
        elif(len(face.vertices)==4):
            f.write(str(mesh.vertices[face.vertices[0]].index)+' ')
            f.write(str(mesh.vertices[face.vertices[1]].index)+' ')
            f.write(str(mesh.vertices[face.vertices[2]].index)+' ')
            f.write('\n')
            f.write(str(mesh.vertices[face.vertices[0]].index)+' ')
            f.write(str(mesh.vertices[face.vertices[2]].index)+' ')
            f.write(str(mesh.vertices[face.vertices[3]].index)+' ')
        f.write('\n')
    f.write('\n')
f.close()
        
#generate the mesh vertices file
print("-------------------------------------")
f=open('vertices.txt','w')
for mesh in bpy.data.meshes:
    print(mesh.name)
    f.write(mesh.name)
    f.write('\n')
    for ver in mesh.vertices:
        print("Vertices:",ver.co)
        f.write(str(ver.co.x)+' '+str(ver.co.y)+' '+str(ver.co.z)+' ')
        f.write('\n')
    f.write('\n')
f.close()

#generate the PySoy Modeller for any general mesh
#PySoy Setup
client = soy.Client()
room = soy.scenes.Room(soy.atoms.Size((8.0,8.0,8.0)))
room['cam'] = soy.bodies.Camera((0,0,5))
client.window.append(soy.widgets.Projector(room['cam']))
room['light'] = soy.bodies.Light((0, 0, 5))
m1 = soy.materials.Colored("red")
m2 = soy.materials.Colored("green")
m3 = soy.materials.Colored("blue")
m4 = soy.materials.Colored("yellow")
room['mesh'] = soy.bodies.Mesh()
room['mesh'].addTorque(10,7,9)	

#Finding Blender Path
path=bpy.app.binary_path
path=path.rstrip(path[-7:])

#open the face mesh file
f=open(path+'mesh_face_details.txt','r')
faces = f.readlines()
mesh=faces[0]

#open the mesh vertices file
v=open(path+'vertices.txt','r')
verts=v.readlines()
c_mesh=verts[0]

def coord(vertex_no,mesh):
	global c_mesh
	no=0
	skip_flag_2=0
	for i in range(1,len(verts)-1): #range(1,len) since the 1st line of the file is mesh name
		if verts[i] == '\n':
			c_mesh=verts[i+1]
			no=0
			skip_flag_2=1

		elif verts[i] != '\n' and c_mesh==mesh:
			if skip_flag_2==0:
				if int(vertex_no)==no:
					verts_co=verts[i].split()
					verts_co[0]=float(verts_co[0])
					verts_co[1]=float(verts_co[1])
					verts_co[2]=float(verts_co[2])
					return(verts_co)
				no+=1 #because the first vertex index= 0
			else:
				skip_flag_2=0

vert_list=[]
face_list=[]
skip_flag_1=0
for i in range(1,len(faces)-1): #range(1,len) since the 1st line of the file is mesh name    
	if faces[i] == '\n':
		mesh=faces[i+1]
		skip_flag_1=1
	elif faces[i] != '\n':
		if skip_flag_1==0:
			face_vert=faces[i].split()

			v_coord=coord(face_vert[0],mesh)
			v1=soy.atoms.Vertex(soy.atoms.Position((v_coord[0],v_coord[1],v_coord[2])),soy.atoms.Vector((0,0,0)) ,soy.atoms.Position((0,0)),soy.atoms.Vector((1,0,0)))
			vert_list.append(v1)

			v_coord=coord(face_vert[1],mesh)
			v2=soy.atoms.Vertex(soy.atoms.Position((v_coord[0],v_coord[1],v_coord[2])),soy.atoms.Vector((0,0,0)) ,soy.atoms.Position((0,0)),soy.atoms.Vector((1,0,0)))
			vert_list.append(v2)

			v_coord=coord(face_vert[2],mesh)
			v3=soy.atoms.Vertex(soy.atoms.Position((v_coord[0],v_coord[1],v_coord[2])),soy.atoms.Vector((0,0,0)) ,soy.atoms.Position((0,0)),soy.atoms.Vector((1,0,0)))
			vert_list.append(v3)

			f1=soy.atoms.Face(v1,v2,v3,m1)
			face_list.append(f1)
			room['mesh'].append(f1)

		else:
			skip_flag_1=0

if __name__ == '__main__' :
	while client.window :
		sleep(.1)
