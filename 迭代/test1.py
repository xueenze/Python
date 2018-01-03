d = {
    'a': 1,
    'b': 2,
    'c': 3
}

# 因为dict的存储不是按照list的方式顺序排列，所以，迭代出的结果顺序很可能不一样
for key in d:
    print(key)

for k,v in d.items():
    print(k,v)

L = [1,5,4,2,3,6,8,10,5]

def findMinAndMax(L):
    if L == []:
        return (None, None)

    min = max = L[0]

    for x in L:
        if max <= x:
            max = x
        if min >= x:
            min = x

    return (min, max)

# 测试
if findMinAndMax([]) != (None, None):
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')
        

findMinAndMax(L)

print(L[2])
