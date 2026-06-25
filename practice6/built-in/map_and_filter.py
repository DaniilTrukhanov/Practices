numbers = [1, 2, 3, 4]
_map = list(map(lambda x: x * x, numbers))
print (_map)

_filter = list(
    filter(
        lambda x: (x % 2) == 0,
        numbers
    )
)
print (_filter)