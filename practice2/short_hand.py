a = 5
b = 2
if a > b: print("a is greater than b")

#if else
a = 2
b = 330
print("A") if a > b else print("B")

#assign a value
a = 10
b = 20
bigger = a if a > b else b
print("Bigger is", bigger)

#multiple conditions in one line
a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")

#ex1
x = 15
y = 20
max_value = x if x > y else y
print("Maximum value:", max_value)

#ex2
username = ""
display_name = username if username else "Guest"
print("Welcome,", display_name)