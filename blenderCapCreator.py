# Importing packages.
import bpy
import numpy as np


# Creates a cap with the following properties.
def createCap(radius, angle, euler, location, corners, layers, name):
    
    # Stores the vertices and faces respectively.
    
    verts = []
    faces = []

    # Creates lists of angles in latitude and longitude.
    
    u = np.linspace(0, 2*np.pi, corners + 1)
    h = np.linspace(np.pi/2 - angle, np.pi/2, layers + 1)

    # Uses the lists of angles to make vertices.

    for phi in h:
        for theta in u:
            x = radius*np.cos(theta)*np.cos(phi)
            y = radius*np.sin(theta)*np.cos(phi)
            z = radius*np.sin(phi)

            vert = (x,y,z)
            verts.append(vert)

    # Creates faces from the vertices.
    
    for j in range(layers):
        for i in range(1, corners + 1):
            
            a = i + j*(corners+1)
            b = (i%corners) + 1 + j*(corners+1)
            c = (i%corners) + 1 + (j+1)*(corners+1)
            d = i + (j+1)*(corners+1)

            face = (a, b, c, d)
            faces.append(face)

    # Define mesh and object.
    
    mesh = bpy.data.meshes.new(name)
    object = bpy.data.objects.new(name, mesh)

    # Set location, rotation and scene of object.
    object.location = location
    object.rotation_euler = euler
    bpy.context.collection.objects.link(object)

    # Create mesh.

    mesh.from_pydata(verts,[],faces)
    mesh.update(calc_edges=True)
    
    # subdivide modifier
    object.modifiers.new("subd", type='SUBSURF')
    object.modifiers['subd'].levels = 3
    object.modifiers['subd'].render_levels = 4
 
    # show mesh as smooth
    #polys = mesh.polygons
    #for p in polys:
    #    p.use_smooth = True