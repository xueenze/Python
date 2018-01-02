def power(x, n):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s

print(power(3, 3))


def enroll(name, gender, age = 6, city = 'Beijing'):
    print('name: ',name)
    print('age: ', age)

enroll('xueenze', '25')

# 不变对象一旦创建，对象内部的数据就不能修改
def add_end(L = None):
    if L is None:
        L = []
    L.append('END')
    return L

print(add_end())

def calc(numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum

print(calc([12]))

def product(*numbers):
    if len(numbers) < 1:
        raise TypeError('1')

    s = 1
    for n in numbers:
        s = s * n
    return s

print('product(5) =', product(5))
print('product(5, 6) =', product(5, 6))
print('product(5, 6, 7) =', product(5, 6, 7))
print('product(5, 6, 7, 9) =', product(5, 6, 7, 9))
if product(5) != 5:
    print('测试失败!')
elif product(5, 6) != 30:
    print('测试失败!')
elif product(5, 6, 7) != 210:
    print('测试失败!')
elif product(5, 6, 7, 9) != 1890:
    print('测试失败!')
else:
    try:
        product()
        print('测试失败!')
    except TypeError:
        print('测试成功!')
    
