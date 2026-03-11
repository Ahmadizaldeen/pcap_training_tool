# Interaktives Tool zum Entfernen von Zeichen

# Benutzer gibt den Originalstring ein
text = input("Gib den Originalstring ein: ")

# Benutzer gibt die Zeichen ein, die entfernt werden sollen
zeichen_entfernen = input("Welche Zeichen sollen entfernt werden? ")

# Neuer String ohne die unerwünschten Zeichen
neuer_text = ''.join(c for c in text if c not in zeichen_entfernen)

# Ausgabe
print("Originalstring:", text)
print("Bereinigter String:", neuer_text)
neuer_text = text[:2] + text[3:] # del index 2 , - gibt es nicht bei str

ord('€')    # → 8364 # code Point
chr(8364)   # → '€'
ord('🐍')    # → 128013 # code Point
chr(128013) # → '🐍'

class A:
    def __init__(self, x=0):
        self.x = x


obj1 = A(2)
obj2 = A(2)
print(id(obj1) == id(obj2))
print(obj1 == obj2)
print(obj1 is obj2)

str1 = 'Hello'
str2 = 'Hello'
print(id(str1) == id(str2))
print(str1 == str2)
print(str1 is str2)

a = 256
b = 256

print(a is b) # true # is nur für Speicher Vergleich benutzen

a = 100000000000000
b = 100000000000000
print(id(a) == id(b)) # true
print(a == b) # true
a = [1,2,3]
b = [1,2,3]
print(a == b) # true
print(a is b) #False

try:
    f = open("non_existing_file", "w")
    print(1, end=" ")
    s = f.readline()
    print(2, end=" ")
except IOError as error:
    print(3, end=" ")
else:
    f.close()
    print(4, end=" ")

class E(Exception):
    def __init__(self, message):
        self.message = message # What a pity
        super().__init__(message)
    def __str__(self): # was ausgegeben wird, wenn das Objekt mit print() angezeigt wird

        return f"it's nice to see you {self.message}"

try:
    print("I feel fine")
    raise E("What a pity")
except E as e:
    print(e) # e.__str__()
else:
    print("the show must go on")



def func(data):
    for d in data[::2]: # von 0 in 2 schritt
        yield d

for x in func('abcdef'):
    print(x, end='')

list1 = [False for i in range(1, 10)]
list2 = list1[-1:1:-1]

data = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]
for i in range(0, 4):
    #print(data[i])
    #print(data[i].pop(), end=' ')
    print(data[i][i], end=' ')
for i in range(len(data)):
    print(data[i][len(data) - 1 - i], end=' ')

def func(x):
    global y
    y = x * x
    return y

func(2)
print(y)

print('ABCDEF'[:3])
print('FEDCBA'[-3:])
print('AXBYCZ'[::2])
print('AXBYCZ'[::-2])

data = [[x for x in range(y)] for y in range(4)]
print(data)
for d in data:
    if len(d) < 2:
        print('*')