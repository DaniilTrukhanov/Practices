def squares(n):
    i = 0
    while i <= n:
        yield (i * i)
        i += 1

for square in squares(5):
    print(square)