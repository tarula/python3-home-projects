lis = [23, 45, 6.45, 's', ['h', 'i', '!']]
lis[1] = 4
lis.append ('HI')
lis.remove (4)
lis.insert (1, 9)

print (lis[2:-2:])

for i in lis:
    print (i, '')

a = 23, 45, 67
print (a)

a = tuple ("Hello")
print (a)

d = {'test' : 45, 'str' : 'Hello!'}
print (d['test'])
print (d['str'])

dic = dict (short='Hi', longer='Hello')
print (dic)
print (dic['short'])

dictationary = dict.fromkeys (['a', 'b', 'c', 'd'], 1)
print (dictationary)

a = set ('Hello')
print (a)

a = frozenset ("Hello")
print (a)

def pr (string, num):
    print (string," ", num)
    pass

def summ (a, b):
    res = a + b
    return res

pr ("Number is", 56)
a = summ (23, 56)
pr('Number is', a)

mult = lambda x, y: x * y
print (mult (2,5))

import math

print (math.e)
print (math.pi)
print (math.cos (1))
print (math.sin (2))

import module as m

m.add ("Hi", " World")

m.add (23, 6)

class Car:
    name = "None"
    height = 1000
    speed = 200.00

    def set (self,name,height, speed):
        self.name = name
        self.height = height
        self.speed = speed

        audi = Car ()
        audi.set ("Audi", 1450,320.30)
        print (audi.name)

    class Truck (Car):
    wheels = 8
    man = Truck ()
    man.wheels = 12
    man.set ("Man", 4500, 140.5)
    print (man.height)
