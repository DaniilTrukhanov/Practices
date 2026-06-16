#creating class
class MyClass:
  x = 5

#creating object
p1 = MyClass()
print(p1.x)

#deleting object
del p1

#multiple objects
p1 = MyClass()
p2 = MyClass()
p3 = MyClass()

print(p1.x)
print(p2.x)
print(p3.x)