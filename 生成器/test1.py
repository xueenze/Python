g = (x * x for x in range(10))

print(next(g))

for n in g:
    print(n)

def add():
    print('step 1')
    yield 1
    print('step 2')
    yield 2
    print('step 3')
    yield 3

o = add()
print(next(o))

def triangles():
    num = [1]
    while True:
        yield num
        num = [num[i] + num[i - 1] for i in range(len(num)) if i != 0]