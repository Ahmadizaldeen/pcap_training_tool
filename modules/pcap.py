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

print("*"*35, 1, '*'*35)
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
print("*"*35)
class A:
    def __init__(self):
        self.val = 5   # Instanzattribut

    def val(self):    # Methode
        return 10

a = A()
print(a.val)
#a.__dict__ = {'val': 5} #überschreibt das Instanzattribut die Methode.
print(A.val(a))
print(a.__dict__)#{'val': 5}
print(A.__dict__['val'])#<function A.val at 0x0000018487AA85C0>
print(a.__dict__['val'])#5
print(A.__dict__)
#Man kann zur Laufzeit Methoden durch Daten überschreiben und wieder zurückbauen.
print("*"*35,"Python-Closure-Effekt")

x = 10
lst = [lambda y: y + i for i in range(3)] # Late Binding (späte Bindung)./"benutze die Variable i aus der Umgebung"
## [lambda y:y +2 , lambda y:y +2,lambda y:y +2]
print([f(0) for f in lst])

lst = [lambda y, i=i : y + i for i in range(3)] # i = 2 letzte aktuliesierung
print([f(3) for f in lst])

x = 5
def func():
    global x
    x += 1
    return x
func()
print(x)
print(f"{func()=}")

x = 5
def func(x):
    x += 1
    #return x
func(x)
func(x)
print(x)
func(x)
print(f"{func(x)=}")

# In Python gilt die LEGB-Scope-Regel:
#
# L → Local
# E → Enclosing
# G → Global
# B → Built-in

print("*"*35,"Shadowing")
a = 10
def f(a):
    a+=1
    return a
print(f(a),a)
print(f(5),a)
print("*"*35,"List Multiplication")
lst = [[0]*3]*3 # * kopiert Referenzen
lst[0][0] = 1
print(lst)
print(id(lst[0]), id(lst[1])), id(lst[2])

lst2 =[ [0]*3 for _ in range(3)]
lst2[0][0] = 1
print(lst2)
print(id(lst2[0]), id(lst2[1])), id(lst2[2])

x = 5
print(id(x))
x= x + 2
print(id(x))
x += 2
print(id(x))
print(x)

y = 9
print(id(y))
y = y +1
print(id(y))
y +=2
print(id(y))

z =[1,2,3]
print(id(z))
z[0] = 99
z[0] +=1
print(z)
print(id(z))

x = "a"
print(id(x))

x += "b"
print(x)
print(id(x))
print("*"*35)

def g():
    yield 1
    yield 2
gen = g()
print(next(gen), next(gen))

a = True
b = False
print(a and not b or b)
#Lösung: True – logische Reihenfolge beachten: and → not → or.
print(b  or b or not b)
