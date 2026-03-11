# Basis-Klassen
class Hund:
    def __init__(self, name, alter):
        self.name = name
        self.alter = alter

    def speak(self):
        print(f"{self.name} ({self.alter} Jahre) sagt Wuff!")

class Katze:
    def __init__(self, name, farbe):
        self.name = name
        self.farbe = farbe

    def speak(self):
        print(f"{self.name} ist {self.farbe} und sagt Miau!")

# Dictionary mit Aliases
tier_klassen = {
    "dog": Hund,
    "puppy": Hund,   # Alias
    "cat": Katze,
    "kitty": Katze   # Alias
}

# Funktion zur dynamischen Objekterstellung mit Parametern
def create_animal(name, *args, **kwargs):
    cls = tier_klassen.get(name)
    if cls:
        return cls(*args, **kwargs)  # Parameter weiterreichen
    else:
        raise ValueError(f"Kein Tier mit dem Namen '{name}' gefunden.")

# Test: Instanzen mit verschiedenen Parametern
tiere = [
    create_animal("dog", "Bello", 3),
    create_animal("kitty", "Luna", "schwarz-weiß"),
    create_animal("puppy", "Fido", 1)
]

for t in tiere:
    t.speak()


#--------------------------------------------------------
# Basis-Klassen
class Hund:
    def __init__(self, name, alter):
        self.name = name
        self.alter = alter

    def speak(self):
        print(f"{self.name} ({self.alter} Jahre) sagt Wuff!")

class Katze:
    def __init__(self, name, farbe):
        self.name = name
        self.farbe = farbe

    def speak(self):
        print(f"{self.name} ist {self.farbe} und sagt Miau!")

# Dictionary mit Aliases
tier_klassen = {
    "dog": Hund,
    "puppy": Hund,   # Alias
    "cat": Katze,
    "kitty": Katze   # Alias
}

# Funktion zur dynamischen Objekterstellung mit Parametern
def create_animal(name, *args, **kwargs):
    cls = tier_klassen.get(name)
    if cls:
        return cls(*args, **kwargs)  # Parameter weiterreichen
    else:
        raise ValueError(f"Kein Tier mit dem Namen '{name}' gefunden.")

# Test: Instanzen mit verschiedenen Parametern
tiere = [
    create_animal("dog", "Bello", 3),
    create_animal("kitty", "Luna", "schwarz-weiß"),
    create_animal("puppy", "Fido", 1)
]

for t in tiere:
    t.speak()