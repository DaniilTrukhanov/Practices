def n_to_0(n):
    while n >= 0:
        yield n
        n -= 1

n = int(input())
for i in n_to_0(n):
    print(i)