t = (1,2,3)
#t[1] = 5 TypeError: 'tuple' object does not support item assignment
l = [1,2,3]
l[0] = 99
s = {1,2,3}
#s[0] = 99TypeError: 'set' object does not support item assignment

for i in range(3):
    if i ==5:
        break
else:
    print("Done")

for i in range (4):
    if i == 2:
        break
else:
    print("Not Done") # break

def f(x=[]):
    x.append(1)
    return x
print(f())
print(f())# das gleiche List-Objekt wird bei jedem Aufruf wiederverwendet

x= 5
def func():
    x+=1
#func() #UnboundLocalError: cannot access local variable 'x' where it is not associated with a value

class A: #klassischer Namenskonflikt zwischen Attribut und Methode.
    def __init__(self):
        self.a = 5 #a.__dict__ = {'val': 5}
    @staticmethod
    def a():
        return 10
    def b(self):
        return 20
obj = A()
print(obj.a) #5 #Python sucht zuerst im Objekt (__dict__ der Instanz) und danach in der Klasse.
print(A.a()) #10 #über dem klasse kann a() aufgerufen, a()
#print(a()) # NameError, a() staticmethod übergesprieben in der Konstruktur
print(obj.b()) # 20
# print(A.b(1))
print(A.b(7)) #, kein static Methode
# print(obj.b())
# print(obj.a)

# # print(a.b)

import math
print(math.trunc(12.00))