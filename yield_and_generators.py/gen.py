def gen_countdown(n):
    while n != 0:
        yield n
        n -= 1


g = gen_countdown(4)
print(next(g))
print(next(g))
print(next(g))


for i in gen_countdown(4):
    print(i)