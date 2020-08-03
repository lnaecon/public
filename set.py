# set.py
from random import randrange

class Set:
    ''' Zelle c11 ex 19 to create a Set. '''

    def __init__(self, elements):
        self.elements = elements

    def add_element(self, x):
        return self.elements.append(x)

    def delete_element(self, x):
        if x in elements:
            self.elements.remove(x)

    def member(self, x):
        if x in self.elements:
            return True
        else:
            return False

    def intersection(self, set2):
        new_set = []
        for i in self.elements:
            if set2.member(i):
                new_set.append(i)
        return Set(new_set)

    def union(self, set2):
        for i in self.elements:
            if not (set2.member(i)):
                set2.add_element(i)
        return set2

    def subtract(self, set2):
        new_set = []
        for i in self.elements:
            if not (set2.member(i)):
                new_set.append(i)
        return Set(new_set)

    def __str__(self):
        text = ""
        for i in self.elements:
            text = text + str(i)
        return text


a = [1, 2, 5]
b = [5, 6, 9]
c = [randrange(1, 10), randrange(1, 10), randrange(1, 10)]
d = [randrange(1, 10), randrange(1, 10), randrange(1, 10)]

ob1 = Set(a)
ob2 = Set(b)
ob3 = Set(c)
print(c, d)
print(ob1.subtract(ob3))







