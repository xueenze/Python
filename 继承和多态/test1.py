class Animal(object):
    def run(delf):
        print('Animal is running......')

class Dog(Animal):
    pass

class Cat(Animal):
    pass

dog = Dog()
dog.run()

cat = Cat()
cat.run()

def run_twice(animal):
    animal.run()
    animal.run()

run_twice(Animal())

# 由运行时的对象的确切类型决定，这就是多态的真正威力
# 对扩展开放
# 对修改封闭