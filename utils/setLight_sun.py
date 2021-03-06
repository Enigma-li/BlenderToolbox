import bpy
import numpy as np

def setLight_sun(rotation_euler, strength, shadow_soft_size = 0.05):
	x = rotation_euler[0] * 1.0 / 180.0 * np.pi 
	y = rotation_euler[1] * 1.0 / 180.0 * np.pi 
	z = rotation_euler[2] * 1.0 / 180.0 * np.pi 
	angle = (x,y,z)
	bpy.ops.object.lamp_add(type = 'SUN', rotation = angle)
	lamp = bpy.data.lamps['Sun']
	bpy.context.object.data.shadow_soft_size = shadow_soft_size
	lamp.node_tree.nodes["Emission"].inputs['Strength'].default_value = strength
	return lamp