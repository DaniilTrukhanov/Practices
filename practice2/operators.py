#python operators
#ex1
print(10 + 5)

#ex2
sum1 = 100 + 50      # 150 (100 + 50)
sum2 = sum1 + 250    # 400 (150 + 250)
sum3 = sum2 + sum2   # 800 (400 + 400)

#arithmetic operators
x = 15
y = 4

print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x % y)
print(x ** y)
print(x // y)

#division in Python
#float
x = 12
y = 5

print(x / y) 

#intger
x = 12
y = 5

print(x // y)

#asignment operators
numbers = [1, 2, 3, 4, 5]

if (count := len(numbers)) > 3:
    print(f"List has {count} elements")

#the ternary operators
num = 6

x = "WEEKEND!" if num > 5 else "Workday"

print(x)

#instead of elif
num = 6

x = "Fri" if num == 5 else "Sat" if num == 6 else "Sun" if num == 7 else "weekday"

print(x)

#comparison operators
x = 5
y = 3

print(x == y)
print(x != y)
print(x > y)
print(x < y)
print(x >= y)
print(x <= y)

#chaining comparison operators
x = 5

print(1 < x < 10)

print(1 < x and x < 10)

#logical operators
#ex1
x = 5

print(x > 0 and x < 10)

#ex2
x = 5

print(x < 5 or x > 10)

#ex3
x = 5

print(not(x > 3 and x < 10))

#identify operators
#ex1
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is z)
print(x is y)
print(x == y)

#ex2
x = ["apple", "banana"]
y = ["apple", "banana"]

print(x is not y)

#membership operators
#ex1
fruits = ["apple", "banana", "cherry"]

print("banana" in fruits)

#ex2
fruits = ["apple", "banana", "cherry"]

print("pineapple" not in fruits)

#membership in strings
text = "Hello World"

print("H" in text)
print("hello" in text)
print("z" not in text)

#Bitwise operators
#ex1
print(6 & 3)

#ex2
print(6 | 3)

#ex3
print(6 ^ 3)

#operator precendence
#ex1 
print((6 + 3) - (6 + 3))

#ex2
print(100 + 5 * 3)

#left-to-right evaluation
print(5 + 4 - 7 + 3)