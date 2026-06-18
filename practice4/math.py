#1
import math

degree = int(input("degree"))
radian = (math.pi/180) * degree

print (round(radian, 6))

#2
height = int(input("Height"))
base1 = int(input("Base first value:"))
base2 = int(input("Base second value:"))
Area = ((base1+base2)/2) * height

print (Area)

#3
import math

n = int(input("Number of sides:"))
l = int(input("Length of a side:"))

a = l / (2 * math.tan(math.pi/n))

area = (n * l * a) / 2
print (round(area, 0))

#4
l = int(input("Length of a base:"))
h = int(input("Height:"))
area = l * h

print (area)