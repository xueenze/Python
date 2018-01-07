def fn(self, name = 'world'):
    print('Hello, %s' % name)

# 动态语言本身支持运行期动态创建类
Hello = type('Hello', (object,), dict(hello=fn))

h = Hello()
h.hello()

# metaclass是类的模板，所以必须从`type`类型派生：
class ListMetaclass(type):
    def __new__(cls, name, bases, attrs):
        attrs['add'] = lambda self, value: self.append(value)
        return type.__new__(cls, name, bases, attrs)