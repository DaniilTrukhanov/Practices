#1
def squares(n):
    i = 0
    while i <= n:
        yield (i * i)
        i += 1

for square in squares(5):
    print(square)

#2
def evens(n):
    i = 0
    while i <= n:
        if (i % 2) == 0:
            yield i
            i += 1
        else:
            i += 1

n = int(input())
print (",".join(str(i) for i in evens(n)))

#3
def divisible(n):
    i = 0
    while i <= n:
        if ((i % 3) == 0) and ((i % 4) == 0):
            yield i
            i += 1
        else:
            i += 1

n = int(input())
for x in divisible(n):
    print(x)

#4
def squares(a, b):
    while a <= b:
        yield (a*a)
        a += 1

a = int(input())
b = int(input())

for i in squares(a, b):
    print (i)

#5
def n_to_0(n):
    while n >= 0:
        yield n
        n -= 1

n = int(input())
for i in n_to_0(n):
    print(i)