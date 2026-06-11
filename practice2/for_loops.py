fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

#looping through a string
for x in "banana":
  print(x)

#break
#ex1
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break
  
#ex2
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)

#comtinue
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)

#range
#ex1
for x in range(6):
  print(x)

#ex2
for x in range(2, 6):
  print(x)

#ex3
for x in range(2, 30, 3):
  print(x)

#else
#ex1
for x in range(6):
  print(x)
else:
  print("Finally finished!")

#ex2
for x in range(6):
  if x == 3: break
  print(x)
else:
  print("Finally finished!")

#nested loops
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)

#pass
for x in [0, 1, 2]:
  pass