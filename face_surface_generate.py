import bpy  
        
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

'''current_obj = bpy.context.active_object    
print("="*40) # printing marker  
for face in current_obj.data.polygons:  
    verts_in_face = face.vertices[:]  
    print("face index", face.index)  
    print("normal", face.normal)  
    for vert in verts_in_face:
        local_point = current_obj.data.vertices[vert].co
        world_point = current_obj.matrix_world * local_point
        print("vert", vert, " vert co", world_point)'''