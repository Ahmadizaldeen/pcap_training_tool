import random
from random import shuffle, choice

# ---------------------------------------------------------------------------
# Fragen-Pool
# ---------------------------------------------------------------------------

def get_question():
    fragen = [

        {
            "frage": "def f():\n    yield 1\n    yield 2\n    yield 3\n\ng = f()\nprint(next(g))",
            "antwort": "1",
            "optionen": ["1", "2", "3", "None"]
        },
        {
            "frage": "def f():\n    yield 1\n    yield 2\n    yield 3\n\ng = f()\nnext(g)\nprint(next(g))",
            "antwort": "2",
            "optionen": ["1", "2", "3", "StopIteration"]
        },
        {
            "frage": "def f():\n    yield 1\n\ng = f()\nprint(type(g).__name__)",
            "antwort": "generator",
            "optionen": ["generator", "list", "function", "iterator"]
        },
        {
            "frage": "def f():\n    yield 1\n    yield 2\n\ng = f()\nlist(g)\nprint(list(g))",
            "antwort": "[]",
            "optionen": ["[]", "[1, 2]", "None", "StopIteration"]
        },
        {
            "frage": "def f():\n    yield 1\n\ng = f()\nnext(g)\nnext(g)  # Was passiert?",
            "antwort": "StopIteration",
            "optionen": ["StopIteration", "None", "0", "GeneratorExit"]
        },
        {
            "frage": "def f():\n    return\n    yield\n\ng = f()\nprint(next(g, 'leer'))",
            "antwort": "leer",
            "optionen": ["leer", "None", "StopIteration", "''"]
        },
        {
            "frage": "g = (x * 2 for x in range(5))\nprint(type(g).__name__)",
            "antwort": "generator",
            "optionen": ["generator", "list", "tuple", "map"]
        },
        {
            "frage": "g = (x * 3 for x in range(5))\nprint(next(g))",
            "antwort": "0",
            "optionen": ["0", "3", "6", "1"]
        },
        {
            "frage": "def f():\n    yield from [1, 2, 3]\n\nprint(list(f()))",
            "antwort": "[1, 2, 3]",
            "optionen": ["[1, 2, 3]", "[[1, 2, 3]]", "None", "1 2 3"]
        },
        {
            "frage": "class Counter:\n    def __init__(self, max):\n        self.max = max\n        self.current = 0\n    def __iter__(self): return self\n    def __next__(self):\n        if self.current < self.max:\n            self.current += 1\n            return self.current\n        raise StopIteration\n\nprint(list(Counter(3)))",
            "antwort": "[1, 2, 3]",
            "optionen": ["[1, 2, 3]", "[0, 1, 2]", "[0, 1, 2, 3]", "[]"]
        },
        {
            "frage": "Welche Aussage zu Generatoren stimmt?",
            "antwort": "Werte werden erst bei Bedarf berechnet",
            "optionen": [
                "Werte werden erst bei Bedarf berechnet",
                "Alle Werte werden sofort gespeichert",
                "Ein Generator ist dasselbe wie eine Liste",
                "next() gibt immer den letzten Wert zurueck"
            ]
        },
        {
            "frage": "Was ist der Vorteil von (x for x in range(1000000))\ngegenueber [x for x in range(1000000)]?",
            "antwort": "Weniger Speicherverbrauch",
            "optionen": [
                "Weniger Speicherverbrauch",
                "Schnellerer Zugriff per Index",
                "Kann mehrfach durchlaufen werden",
                "Unterstuetzt mehr Datentypen"
            ]
        },
    ]

    return choice(fragen)


# ---------------------------------------------------------------------------
# Optionen mischen
# ---------------------------------------------------------------------------

def generate_options(frage_dict):
    optionen = frage_dict["optionen"][:]
    shuffle(optionen)
    return optionen


# ---------------------------------------------------------------------------
# User Input
# ---------------------------------------------------------------------------

def user_input(anzahl_optionen):
    invalid_input = 0
    while True:
        user_answer = input("Deine Antwort: ")
        try:
            user_answer = int(user_answer)
            if 1 <= user_answer <= anzahl_optionen:
                return user_answer
            else:
                raise ValueError
        except ValueError:
            invalid_input += 1
            if invalid_input < 3:
                print(f"Ungueltige Eingabe. Du hast noch {3 - invalid_input} Versuche.")
            else:
                print("Programm wird beendet.")
                exit(0)


# ---------------------------------------------------------------------------
# run_generator
# ---------------------------------------------------------------------------

def run_generator(progress):
    frage_dict = get_question()

    print("\n--- Generatoren & Iteratoren Quiz ---")
    print(frage_dict["frage"])
    print()

    optionen = generate_options(frage_dict)

    for i, opt in enumerate(optionen, start=1):
        print(f"{i}. {opt}")

    richtige_antwort = frage_dict["antwort"]
    richtiger_index = optionen.index(richtige_antwort) + 1

    user = user_input(len(optionen))

    if user == richtiger_index:
        print("Richtig ✅")
    else:
        print(f"Falsch ❌  Richtig: {richtiger_index}. {richtige_antwort}")

    progress.add_attempt(
        module_name="generatoren",
        question=frage_dict["frage"].splitlines()[0],
        user_answer=user,
        correct_answer=richtiger_index,
    )


# ---------------------------------------------------------------------------
if __name__ == "__main__":
    from modules.progress_utils import ProgressManager
    p = ProgressManager("progress.json")
    run_generator(p)