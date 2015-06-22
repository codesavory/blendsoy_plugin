#Python Script to extend blender to model objects and convert it to pysoy 
import bpy
import os

ob = bpy.data.objects['Cube']
print("-------------------------------")
for v in ob.data.vertices:
    mat = ob.matrix_world
    # Multiply matrix by vertex
    loc = mat * v.co
    print(loc)

#Initial PySoy Setup
def Initiate():
    f.write("""#!/usr/bin/python3.4
import soy
from time import sleep

client = soy.Client() #Setting up client window
room = soy.scenes.Room(soy.atoms.Size((15.0, 15.0, 15.0))) #Creating a room scene with room size=15
room['camera'] = soy.bodies.Camera(soy.atoms.Position((0,0,5))) #adding camera to the scene
room['light'] = soy.bodies.Light(soy.atoms.Position((-2,3,5))) #adding lighting to the scene
client.window.append(soy.widgets.Projector(room['camera']))
client.window.background = soy.atoms.Color('white')

if __name__ == '__main__':""")

#Creating PySoy Code goes here:
def SoyModel():
    Initiate()
    for mesh in bpy.data.meshes:
        if(mesh.name=='Cube'):
            f.write("""room['cube'] = soy.bodies.Box()
room['cube'].addTorque(10, 10, 10)
room['cube'].material=soy.materials.Colored('red')
while client:
	sleep(.1)""")
    
    f.close()
    #Finding Blender Path
    path=bpy.app.binary_path
    path=path.rstrip(path[-7:])
    #Creating Command to execute PySoy File Created
    cmd="python3 "+path+"workfile.py"
    os.system(cmd)

if __name__ == '__main__':
    f = open('workfile.py', 'w')
    SoyModel()
