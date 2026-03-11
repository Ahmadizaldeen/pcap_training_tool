# decorators_demo.py

# =============================
# Normale Funktions-Decorator
# =============================
def func_decorator(func):
    def wrapper(*args, **kwargs):
        print(">> Vor der normalen Funktion")
        result = func(*args, **kwargs)
        print(">> Nach der normalen Funktion")
        return result
    return wrapper

@func_decorator
def say_hello(name):
    print(f"Hallo, {name}!")

# =============================
# Lambda-Decorator Beispiel
# =============================
def lambda_decorator(f):
    return lambda x: f"Lambda-Dekorator: {f(x)}"

@lambda_decorator
def square(x):
    return x * x

# =============================
# Klassen-Decorator
# =============================
class ClassDecorator:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print(">> Vor der Klassen-Dekoration")
        result = self.func(*args, **kwargs)
        print(">> Nach der Klassen-Dekoration")
        return result

@ClassDecorator
def greet(msg):
    print(msg)

# =============================
# Eingebaute Decorators: @staticmethod & @classmethod
# =============================
class MyClass:
    class_var = "Klassenvariable"

    @staticmethod
    def static_method():
        print(">> Dies ist eine statische Methode")

    @classmethod
    def class_method(cls):
        print(f">> Dies ist eine Klassenmethode, cls.class_var = {cls.class_var}")

# =============================
# Testfunktion, alle ausführen
# =============================
def run_demo():
    print("\n--- Normale Funktions-Decorator ---")
    say_hello("Ahmad")

    print("\n--- Lambda-Decorator ---")
    print(square(5))

    print("\n--- Klassen-Decorator ---")
    greet("Willkommen!")

    print("\n--- Static- und Classmethod ---")
    MyClass.static_method()
    MyClass.class_method()


# =============================
# Ausführung direkt über Modul
# =============================
if __name__ == "__main__":
    run_demo()