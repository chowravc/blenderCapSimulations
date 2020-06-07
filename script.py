import bpy
import sys
import os
import numpy as np
import random as r

dir = os.path.dirname(bpy.data.filepath)
if not dir in sys.path:
    sys.path.append(dir)
import blenderCapCreator as bCC

# Creating the floor and walls.
# mesh arrays
verts = [(-3, -3, 0), (-3, 3, 0), (3, 3, 0), (3, -3, 0)]
faces = [(1, 2, 3, 4)]

# Define mesh and object.
    
mesh = bpy.data.meshes.new("Floor")
object = bpy.data.objects.new("Floor", mesh)

# Set location, rotation and scene of object.
object.location = location
object.rotation_euler = euler
bpy.context.collection.objects.link(object)

# Create mesh.

mesh.from_pydata(verts,[],faces)
mesh.update(calc_edges=True)

# Creating a number of randomly decided caps.

# Number of random caps to create.
number = 5

# Radius of the sphere the cap will be on.
radius = 1

# Location of the cap.
location = (0, 0, 0)

# Number of corners the cap will have on the xy plane.
corners = 8

# Number of layers being stacked in the z direction.
layers = 6

for i in range(number):
    # Angular size of the cap.
    angle = r.random()*np.pi/10

    # Euler angles of the cap.
    euler = (r.random()*2*np.pi, r.random()*np.pi, 0)
    
    # Name the cap.
    name = "Cap"+str(i)
    
    bCC.createCap(radius, angle, euler, location, corners, layers, name)
    
'''
# Change these variables to make a cap.
# Radius of the sphere the cap will be on.
radius = 1

# Angular size of the cap.
angle = np.pi/10

# Euler angles of the cap.
euler = (0, 0, 0)

# Location of the cap.
location = (0, 0, 0)

# Number of corners the cap will have on the xy plane.
corners = 8

# Number of layers being stacked in the z direction.
layers = 6

# Name the cap.
name = "Cap"

bCC.createCap(radius, angle, euler, location, corners, layers, name)
'''
