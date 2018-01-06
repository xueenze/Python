print(type(123))

print(type(abs))

import types

def fn():
    pass

print(type(fn) == types.FunctionType)

class Test(object):
    def methodTest(self):
        print('test')

test = Test()

print(type(test))

print(isinstance(test, Test))

# 总是优先使用isinstance()判断类型，可以将指定类型及其子类一网打尽

print(dir(test))