
def apply_func(x, func):
    return func(x)

def closure_example(msg):
    def inner():
        return f"Closure sagt: {msg}"
    return inner

#
if __name__ == "__main__":
    books = ["Python", "AI", "Datenbanken"]

    def apply(rule, value):
        return rule(value)

    print(apply(lambda title: len(title) > 3, "Python"))

    def f(a, b):
        if callable(a):
            return a(b)
        raise TypeError("a muss eine Funktion sein")

    def apply_filter(check, value):
        return check(value)

    print(apply_filter(lambda title: len(title) > 3 and True, "Python"))

    def f(a, b):
        return a(b)
    print(f(lambda x: x and True, 1 > 0))

    def foo(x,y,z):
        return x(y) - x(z)

    print(foo(lambda x: x % 2, 2, 1))


    text = "I'm gonna make him an offer he can't refuse"
    words = text.split()
    length = list(map(lambda word: len(word), words))
    print(length)

