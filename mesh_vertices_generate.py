import bpy
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
'''x=input("Continue:")
    if(x=='y'):
        continue '''