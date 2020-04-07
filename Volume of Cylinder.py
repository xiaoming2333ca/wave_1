import math

base_radius = int(input("please enter the base radius of cylinder: "))
height = int(input("please enter the height of cylinder: "))

base_area = math.pi * pow(base_radius, 2)
cylinder_volume = base_area * height

print(cylinder_volume)
