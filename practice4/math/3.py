import math

n = int(input("Number of sides:"))
l = int(input("Length of a side:"))

a = l / (2 * math.tan(math.pi/n))

area = (n * l * a) / 2
print (round(area, 0))