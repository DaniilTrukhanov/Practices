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