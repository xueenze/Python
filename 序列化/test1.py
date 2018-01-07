import pickle

d = dict(name = 'Bob', age = 20, score = 88)
print(pickle.dumps(d))

f = open('test.txt', 'wb')
d = pickle.dump(d, f)
f.close()

f = open('test.txt', 'rb')
d = pickle.load(f)
f.close()

print(d)

import json

json.dumps(d)

class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

s = Student('Bob', 20, 88)

print(json.dumps(s, default = lambda obj: obj.__dict__))

def dict2student(d):
    return Student(d['name'], d['age'], d['score'])

json_str = '{"age": 20, "score": 88, "name": "Bob"}'
print(json.loads(json_str, object_hook=dict2student))