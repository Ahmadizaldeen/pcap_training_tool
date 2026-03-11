class A:
    def __init__(self):
        self.name = ""
    def foo(self):
        print("foo")
    a = 10

a =A()
#print(A.__dict__)
#print(a().__dict__)

class Car:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

c = Car("BMW", 2020)

print(c.__dict__)

class Test:
    x = 10

    def hello(self):
        return "hi"

print(Test.__dict__)

class A:
    x = 10

    def __init__(self):
        self.y = 20

a = A()

print(A.__dict__) #Klassenattribute + Methoden
print(a.__dict__) #Instanzattribute