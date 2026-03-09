from faker import Faker
from random import choice, shuffle, randint

fake = Faker()

# Alle Methoden, die wir testen wollen
string_funktionen = [
    ["split","String → Liste"],
    ["strip","Entfernt Leerzeichen oder andere Zeichen"],
    ["Palindrom","Schreibe Text rückwärts [::-1]"],
    ["replace","Ersetzt Teilstring"],
    ["count","Zählt Vorkommen"],
    ["startswith","Prüft Anfang"],
    ["endswith","Prüft Ende"],
    ["casefold","aggressive Kleinschreibung"],
    ["join","Liste → String"],
    ["index","wie find(), wirft Fehler wenn nicht gefunden"],
    ["find","gibt Position oder -1"],
    ["rfind","gibt Position oder -1"],
    ["upper","alles GROSS"],
    ["lower","alles klein"],
    ["title","Jedes Wort Groß"],
    ["capitalize","erster Buchstabe groß"],
    ["sorted","Liste von Zeichen"],
    ["sort","❌ kein String Method"]
]

# Methoden in Gruppen
func_dict = {
    "general_method": ["index","find","rfind"],
    "text_method": ["split","strip","replace","title","capitalize"],
    "word_method": ["join","upper","lower"],
    "liter_method": ["count","startswith","endswith","sorted"],
    "other_method": ["Palindrom","casefold","sort"]
}

# Zufällige Methode auswählen
def get_method():
    return choice([item[0] for item in string_funktionen])

# Zufälligen Text, Wort, Buchstaben generieren
def text_generator():
    text = fake.text(70)
    words = [w.strip(".,'") for w in text.split()]
    word = choice(words)
    litter = list(choice(words))
    return text, word, litter

# Frage anzeigen
def set_question(func_name, text, word, litter):
    if func_name in func_dict["text_method"]:
        if func_name == "replace":
            replace_with = choice(text.split())
            print(f'Was ist das Ergebnis von: "{text}".replace("{word}", "{replace_with}")')
        elif func_name == "split":
            zeichen = choice([",", ".", "!"])
            print(f'Was ist das Ergebnis von: "{text}".split("{zeichen}")')
        else:
            print(f'Was ist das Ergebnis von: "{text}".{func_name}()')
    elif func_name in func_dict["word_method"]:
        if func_name == "join":
            join_with = choice([",", ".", "!"])
            print(f'Was ist das Ergebnis von: "{join_with}".join("{text}")')
        else:
            print(f'Was ist das Ergebnis von: "{word}".{func_name}()')
    else:
        print(f'Was ist das Ergebnis von: {func_name}("{word}")')

# Antwort berechnen
def string_quiz(func_name, text, word, litter):
    methods = {
        "upper": lambda w,t,l: w.upper(),
        "lower": lambda w,t,l: w.lower(),
        "sorted": lambda w,t,l: sorted(w),
        "count": lambda w,t,l: t.count(l),
        "startswith": lambda w,t,l: t.startswith(w),
        "endswith": lambda w,t,l: t.endswith(w),
        "title": lambda w,t,l: t.title(),
        "capitalize": lambda w,t,l: t.capitalize(),
        "casefold": lambda w,t,l: w.casefold(),
        "Palindrom": lambda w,t,l: w[::-1],
    }

    if func_name in methods:
        return methods[func_name](word, text, litter)
    if func_name == "index":
        try:
            return text.index(word)
        except ValueError:
            return "ValueError"
    if func_name == "find":
        return text.find(word)
    if func_name == "rfind":
        return text.rfind(word)
    if func_name == "sort":
        return "kein String Method"
    return "nicht implementiert"

# Optionen für Multiple Choice generieren
def generate_options(correct, options_list=None):
    options = [correct]
    while len(options) < 4:
        fake_option = choice(options_list) if options_list else fake.word()
        if fake_option not in options:
            options.append(fake_option)
    shuffle(options)
    return options

# Hauptfunktion
def run_string_quiz():
    func_name = get_method()
    text, word, litter = text_generator()
    set_question(func_name, text, word, litter)
    answer = string_quiz(func_name, text, word, litter)
    print("\nRichtige Antwort:", answer)
    options = generate_options(answer, text.split())
    print("Optionen:", options)

if __name__ == "__main__":
    run_string_quiz()