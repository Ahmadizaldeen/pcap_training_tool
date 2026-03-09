data = [[0, 1, 2, 3] for i in range(3)]
print(data)
print(data[2][0])
#import coml
z = 3+4j#<class 'complex'>, j steht für √−1.
#z.real      # 3.0
#z.imag      # 4.0
#abs(z)      # 5.0  (Betrag, also √(3²+4²))
print(type(1J))#<class 'complex'>
#(3+4j) > (1+2j)#Es gibt kein „größer“ oder „kleiner“ im komplexen Zahlenraum.
z1 = complex(2,5)#numerische Typen-Hierarchie (int → float → complex)

add = (1+2j) + (3+4j)
mul = (1+2j)*(3+4j)#= 3 + 4j + 6j + 8j² = 3 + 10j + 8(-1) = -5 + 10j
abswert = abs(3+4j)

class MyComplex:
    def __init__(self, real, imag):
        self.real = float(real)
        self.imag = float(imag)

    def __str__(self):
        return f"{self.real} + {self.imag}j"

    def __add__(self, other):#Methoden müssen ein neues Objekt zurückgeben
        return MyComplex(
            self.real + other.real,
            self.imag + other.imag
        )

    def __mul__(self, other):
        real_part = self.real * other.real - self.imag * other.imag
        imag_part = self.real * other.imag + self.imag * other.real
        return MyComplex(real_part, imag_part)

z1 = MyComplex(1, 2)
z2 = MyComplex(3, 4)
print(z2)
print(z1 + z2)
print(z1*z2)

c, b, a = 1, 3, 2 #(1,3,2)

#orginal_tupel ((1,3,2)) mit rechte seite Evaluation
#c, b, a = b, a, c # (c,b,a) = (3,2,1) ->print(a, b, c) = print(1, 2, 3)
c, b, a = a, c, b # (c,b,a) = (2,1,3) ->print(a, b, c) = print(3,1,2)
#a, b, c = c, a, b # (a,b,c) = (1,2,3) ->print(a, b, c) = print(1,2,3)
#a, b, c = a, b, c # (a,b,c) = (2,3,1) ->print(a, b, c) = print(2,3,1)
print(a, b, c) #die ursprünglichen Werte auf der linken Seite werden nicht verändert, bevor die rechte Seite komplett evaluiert ist.


data = [[x for x in range(y)] for y in range(3)]
print(data)
from random import randint
print(randint(1, 3), end='')

print("[Question 18] Which of the following expressions evaluate to True?")

print((ord("0") - ord("9")), "== 10")
print(ord("0") , ord("9"))
print(len("''") == 2)
print(chr(ord('z') - 1) == 'y')
print("len(''1234'') == 4")


import keyword
print(keyword.kwlist)

# Stack mit Liste
stack = []

# Push (Element hinzufügen)
stack.append(1)
stack.append(2)
stack.append(3)

print("Stack nach Push:", stack)

# Pop (Element entfernen, oben zuerst)
top = stack.pop() #Letztes Element, das reinkommt (3), wird als erstes entfernt → LIFO ✅
print("Pop Element:", top)
print("Stack danach:", stack)

# Queue mit Liste
queue = []

# Enqueue (Element hinzufügen)
queue.append(1)
queue.append(2)
queue.append(3)

print("Queue nach Enqueue:", queue)

# Dequeue (Element entfernen, vorne zuerst)
front = queue.pop(0) #Erstes Element, das reinkommt (1), wird als erstes entfernt → FIFO ✅
print("Dequeue Element:", front)
print("Queue danach:", queue)
# Stack = append + pop() → LIFO
#
# Queue = append + pop(0) → FIFO (alternativ collections.deque für effizientere Queue)

x = 1 / 2 + 3 // 3 + 4 ** 2

print(x)


x = 16

while x > 0:
    print('*')
    print(x)
    x //= 2 #x //= 2 → x = x // 2 (Ganzzahl-Division)
print(x)


def increment(c, num):
    c.count += 1
    num += 1

class Counter:
    def __init__(self):
        self.count = 0

counter = Counter()
number = 0

for i in range(0, 100):
    increment(counter, number)
print(
    "counter is "
    + str(counter.count)
    + ", number of times is "
    + str(number)
)

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass  # Muss von jeder Subklasse implementiert werden

class Circle(Shape):
    def __init__(self, r):
        self.radius = r

    def area(self):
        return 3.14 * self.radius ** 2

# Shape()  # ❌ Error, kann nicht direkt instanziiert werden
c = Circle(5)  # ✅ funktioniert
print(c.area())

from abc import ABC, abstractmethod

# =========================
# Abstract Class
# =========================
class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass  # Muss von Subklasse implementiert werden

    def info(self):
        print("Dies ist ein Fahrzeug.")  # konkrete Methode möglich

# =========================
# Subklasse
# =========================
class Car(Vehicle):
    def start_engine(self):
        print("Auto-Motor gestartet!")

# =========================
# Test
# =========================
# vehicle = Vehicle()  # ❌ Error: kann nicht direkt instanziiert werden
my_car = Car()         # ✅ Subklasse kann instanziert werden
my_car.info()          # ruft konkrete Methode aus Abstract Class
my_car.start_engine()  # ruft implementierte abstrakte Methode
# Was passiert hier für PCAP
#
# Vehicle ist Abstract Class → kann nicht direkt instanziiert werden
#
# Car implementiert die abstrakte Methode start_engine → Instanziierung möglich
#
# Vehicle kann konkrete Methoden wie info() enthalten → Subklasse erbt sie

z = 2
y = 1
x = y < z or z > y and y > z or z < y
print(x)

from faker import Faker

fake = Faker()
print(fake.name())
print(fake.email())
print(fake.text())