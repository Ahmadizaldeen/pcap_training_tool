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


BLUE = '\033[94m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
RED = '\033[0;31m'
CYAN = '\033[96m'
MAGENTA = '\033[95m'
ENDC = '\033[0m'

def colorize(value):

    if isinstance(value, int):
        color = BLUE
    elif isinstance(value, float):
        color = MAGENTA
    elif isinstance(value, str):
        color = GREEN
    elif isinstance(value, list):
        color = CYAN
    elif isinstance(value, dict):
        color = YELLOW
    elif isinstance(value, tuple):
        color = RED
    else:
        color = ENDC

    return f"{color}{value}{ENDC}"

def type_color_decorator(func):
    print(f"{BLUE}int {GREEN}str {YELLOW}dict {RED}list {CYAN}list {MAGENTA}float{ENDC}")

    def wrapper(*args, **kwargs):

        result = func(*args, **kwargs)

        return colorize(result)

    return wrapper

def debug(func):

    def wrapper(*args, **kwargs):

        print(f"[DEBUG] Function: {func.__name__}")
        print(f"[DEBUG] args: {args}")
        print(f"[DEBUG] kwargs: {kwargs}")

        result = func(*args, **kwargs)

        print(f"[DEBUG] result: {result}")

        return result

    return wrapper

def colored_class(default_color):
    RESET = '\033[0m'
    def decorator(cls):
        original_str = cls.__str__ if hasattr(cls, "__str__") else lambda self: f"{self.__class__.__name__}"

        def new_str(self):
            return f"{default_color}{original_str(self)}{RESET}"

        cls.__str__ = new_str
        return cls

    return decorator

if __name__ == "__main__":

    print(f"{BLUE}int {GREEN}str {YELLOW}dict {RED}list {CYAN}list {MAGENTA}float{ENDC}")
    run_demo()