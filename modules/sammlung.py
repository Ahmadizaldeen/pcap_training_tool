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