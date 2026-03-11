import doctest


# ANSI Farben
BLUE = '\033[94m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
RED = '\033[0;31m'
CYAN = '\033[96m'
MAGENTA = '\033[95m'
WHITE   = '\033[47m'
ENDC = '\033[0m'

def type_color_decorator(func):
    """
    Decorator, der alle Argumente nach Typ einfärbt und an die Originalfunktion weitergibt
    """
    def wrapper(self, *args, **kwargs):
        new_args = []
        # Alle positional args einfärben
        for arg in args:
            if isinstance(arg, int):
                color = BLUE
            elif isinstance(arg, float):
                color = GREEN
            elif isinstance(arg, str):
                color = YELLOW
            elif isinstance(arg, list):
                color = RED
            elif isinstance(arg, dict):
                color = MAGENTA
            elif isinstance(arg, tuple):
                color = CYAN
            else:
                color = WHITE
                color = ENDC
            new_args.append(f"{color}{arg}{ENDC}")

        # Keyword args einfärben
        new_kwargs = {}
        for k, v in kwargs.items():
            if isinstance(v, int):
                color = BLUE
            elif isinstance(v, float):
                color = GREEN
            elif isinstance(v, str):
                color = YELLOW
            elif isinstance(v, list):
                color = RED
            elif isinstance(v, dict):
                color = MAGENTA
            elif isinstance(v, tuple):
                color = CYAN
            else:
                color = ENDC
            new_kwargs[k] = f"{color}{v}{ENDC}"

        # Originalfunktion mit eingefärbten args/kwargs aufrufen
        return func(self, *new_args, **kwargs)

    return wrapper

def type_color_decorator_old(func):

    """
    Decorator, der die Ausgabe farblich nach Datentyp einfärbt
    """
    def wrapper(value):
        # Farbe nach Typ bestimmen
        if isinstance(value, int):
            color = BLUE
        elif isinstance(value, float):
            color = GREEN
        elif isinstance(value, str):
            color = YELLOW
        elif isinstance(value, list):
            color = RED
        elif isinstance(value, dict):
            color = MAGENTA
        elif isinstance(value, tuple):
            color = CYAN
        else:
            color = ENDC  # default

        # Originalfunktion aufrufen, aber mit eingefärbtem Text
        return func(f"{color}{value}{ENDC}")
    return wrapper

if __name__ == '__main__':
    class Test :

        @type_color_decorator
        def add(self,x,y):
            return x+y

    test = Test()
    print(test.add("1",2))
    # print(add(2,3))
    # add(3,5)


    # Farben definieren
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[0;31m'
    ENDC = '\033[0m'


    # Funktion zum farbigen Ausgeben
    def print_colored(message, level="info"):
        """
        message: Text, der ausgegeben wird
        level: 'info', 'success', 'warning', 'error'
        """
        if level == "info":
            color = BLUE
        elif level == "success":
            color = GREEN
        elif level == "warning":
            color = YELLOW
        elif level == "error":
            color = RED
        else:
            color = ENDC  # Standardfarbe

        print(f"{color}{message}{ENDC}")


    # Beispiele
    print_colored("Das ist eine Info", "info")
    print_colored("Alles erfolgreich erledigt!", "success")
    print_colored("Achtung, etwas stimmt nicht!", "warning")
    print_colored("Fehler aufgetreten!", "error")