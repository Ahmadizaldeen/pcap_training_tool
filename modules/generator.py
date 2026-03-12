def f(n):
    for i in range(1, n+1):
        yield i*i # Python erstellt automatisch __iter__() & __next__().
g = f(5)
print(g)#<generator object f at 0x000002A063BEA960>
print(type(g))
print(next(g))
print(next(g))
print(list(g))
print(list(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
g = (i for i in range(3))

print(next(g))
print(next(g))

def f():
    yield 1
    yield 2

g = f()

print(next(g))
print(list(g))

def f():
    yield 1
    yield 2

g1 = f()
g2 = f()

print(next(g1))
print(next(g2))

def f():
    yield 1
    yield 2

g = f()

print(list(g))
print(list(g))

class Counter:
    def __init__(self, max):
        self.max = max
        self.current = 0
    def __iter__(self):
        return self
    def __next__(self):
        if self.current < self.max:
            self.current += 1
            return self.current
        else:
            raise StopIteration

c = Counter(3)
print(next(c))  # 1
print(next(c))  # 2

