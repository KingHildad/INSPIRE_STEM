# This is code used to calculate the surface area of a sphere
# Date:21/02/2024
# Name:Hildad

Radius=float(input("Enter the Radius of the cylinder:"))
Height=float(input("Enter the height of the cylinder:"))
Py=float(3.142)
Diameter=float(Radius*2)

Surface_area=float((2*Py*(Radius**2)))

print("The surface area is",Surface_area)
