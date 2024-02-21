#A program to solve a quadratic eqn
#Date:20/02/2024
#Name:Hildad Ndungu

import math

a=float(input({"Enter the coeffecient of the first term:"}))
b=float(input({"Enter the coeffecient of the second term:"}))
c=float(input({"Enter the contant:"}))
d=((float(b**2))-(float(4*a*c)))

x_1=( ((-b)+(math.sqrt(d))))/2*a

print("The value of the quadratic eqn is",x_1)




