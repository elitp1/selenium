def a():
    print("1")
    yield 1
    print("2")
    yield 3

p = a()
print(next(p))
print(next(p))


