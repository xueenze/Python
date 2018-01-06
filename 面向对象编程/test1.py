# -*- coding: utf-8 -*-

class Student(object):
    def __init__(self, name, score):
        self.__name = name
        self.__score = score
    
    def set_score(self, score):
        self.__score = score

    def print_score(self):
        print('%s: %s' % (self.__name, self.__score))

    def get_grade(self):
        if self.__score >= 90:
            return 'A'
        elif self.__score >= 60:
            return 'B'
        else:
            return 'C'

bart = Student('Bart', 98)

bart.print_score()
print(bart.get_grade())

bart.test = 1
print(bart.test)

# Python本身没有任何机制阻止你干坏事，一切全靠自觉
