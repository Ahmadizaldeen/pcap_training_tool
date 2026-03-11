
from functools import wraps

def my_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Vor Ausführung von {func.__name__}")
        result = func(*args, **kwargs)
        print(f"Nach Ausführung von {func.__name__}")
        return result
    return wrapper

class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, r):
        if r < 0:
            raise ValueError("Radius muss positiv sein")
        self._radius = r

    @property
    def area(self):
        return 3.1415 * self._radius ** 2

class A:
    def greet(self):
        print("Hallo von A")

class B:
    def greet(self):
        print("Hallo von B")

class C(A,B):
    pass

# -------------------------------
# Dekorator für Eingabevalidierung
# -------------------------------
import re
from functools import wraps


def validate_user_input(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        user_info = func(*args, **kwargs)

        # Validierung
        if not user_info["username"]:
            raise ValueError("Username darf nicht leer sein")
        if not re.match(r"[^@]+@[^@]+\.[^@]+", user_info["email"]):
            raise ValueError("Ungültige E-Mail")
        if len(user_info["password"]) < 4:
            raise ValueError("Passwort zu kurz")
        return user_info
    return wrapper
