

from faker import Faker
from random import shuffle, choice, randint
fake = Faker()

string_funktionen = [["split","String → Liste"],
                     ["strip","Entfernt Leerzeichen (oder andere Zeichen, wenn angegeben)"],
                     ["Palindrom","[::-1] Schreibe den Text rückwärts"],
                     ["replace","ersetzt Teilstring" ],
                     ["count","zählt Vorkommen" ],
                     ["startswith","Anfang prüfen" ],
                     ["endswith","Ende prüfen"],
                     ["casefold","aggressive Kleinschreibung (für Vergleiche)"],
                     ["join","Liste → String"],
                     ["index","wie find(), aber wirft Fehler" ],
                     ["find","gibt Position oder -1, Sucht von links nach rechts." ],
                     ["rfind","gibt Position oder -1,Sucht von rechts nach links." ],
                     ["upper","alles GROSS"],
                     ["lower","alles klein"],
                     ["title","Jedes Wort Groß"],
                     ["capitalize","erster Buchstabe groß"],
                     ["sorted", "Das Ergebnis ist eine Liste von Zeichen"],
                     ["sort", "❌ AttributeError bei str"]]


func_dict = {"general_method" : ["index","find","rfind"],
             "text_method" : ["split","strip","replace", "title","capitalize" ],
             "word_method" :["join","upper","lower"],
             "liter_method" : ["count","startswith","endswith","sorted"],
             "other_method":["Palindrom","casefold","sort"]}

def get_method():
    all_method = [item[0] for item in string_funktionen]
    choiced_method = choice(all_method)
    return choiced_method

def text_generator():
    fake_text = fake.text(70)
    text = fake_text
    fake_words = [w.strip(".,'") for w in fake_text.split()]
    fake_litter = list(fake_words[0] + fake_words[1])
    rnd_ind_liter = randint(0, len(fake_litter) - 1)
    liter = fake_litter[rnd_ind_liter]
    rnd_ind_word = randint(0, len(fake_words) - 1)
    word = fake_words[rnd_ind_word]
    return text, word, liter


def set_question(func_name,text, word, liter):
    if func_name in func_dict.get("general_method"): #["index", "find", "rfind"],
        print(text)
        print( f"what is the output from : {func_name}({word})")

    elif func_name in func_dict.get("text_method"): #["split", "strip", "replace", "title", "capitalize"]
        if func_name == "replace":
            replace_with = choice(text.split())
            print(f"what is the output from : {func_name}({word},{replace_with})")
        elif func_name == "title":
            print(f'what is the output from : {func_name}("{text}")')
        elif func_name == "strip":
            print(f'what is the output from : {func_name}("{text}")')
        elif func_name == "split":
            zeichen = choice([",", ".", "!"])
            print(f'what is the output from: "{text}".split("{zeichen}")')
        else:
            print(f"what is the output from : {func_name}({word})")


    elif func_name in func_dict.get("word_method"):#["join", "upper", "lower"]
        if func_name == "join":
            join_with = choice(",.!")
            print(f"what is the output from : {join_with}.{func_name}({word})")
        else:
            print(f"what is the output from : {func_name}({word})")


    elif func_name in func_dict.get("liter_method"):#["count", "startswith", "endswith", "sorted"]
        if func_name == "count":
            print(f"what is the output from : {func_name}({liter})")
        else:
            print(f"what is the output from : {func_name}({word})")

        print(text)


    elif func_name in func_dict.get("other_method"):
        print(f"what is the output from : {func_name}({word})")
        print(text)

    return word

def generate_options(correct, options_list=None):
    options = [correct]
    while len(options) < 4:
        fake_option = choice(options_list) if options_list else fake.word()
        if fake_option not in options:
            options.append(fake_option)
    shuffle(options)
    return options

def string_quiz (func_name,text, word, liter):
    answer, zeichen = None, None

    if func_name in func_dict.get("general_method"): #["index", "find", "rfind"],
        if func_name == "index":
            answer = text.index(word)
            print(answer)
        elif func_name == "find" :
            answer = text.find(word)
            print( answer)
        elif func_name == "rfind" :
            answer = text.rfind(word)
            print( answer)

    elif func_name in func_dict.get("text_method"):
        #["split", "strip", "replace", "title", "capitalize"]
        if func_name == "split":
            zeichen = choice([",", ".", "!"])
            answer = text.split(zeichen)
            print( answer)
        elif func_name == "strip":
            zeichen = choice([",", ".", "!"])
            answer = text.strip(zeichen)
            print( answer)
        elif func_name == "replace":
            replace_with =fake.word()
            answer = text.replace(word,replace_with)
            print( answer)
        elif func_name == "title":
            answer = text.title()
            print( answer)
        elif func_name == "capitalize":
            answer = text.capitalize()
            print( answer)


    elif func_name in func_dict.get("word_method"):
        #["join", "upper", "lower"]
        if func_name == "join":
            join_with =choice([",", ".", "!"])
            answer = join_with.join(text.split())
            print(answer)
        elif func_name == "upper":
            answer = word.upper()
            print( answer)
        elif func_name == "lower":
            answer = word.lower()
            print( answer)


    elif func_name in func_dict.get("liter_method"):
        #["count", "startswith", "endswith", "sorted"]
        if func_name == "count":
            answer = text.count(liter)
            print( answer)
        elif func_name == "startswith":
            answer = text.startswith(word)
            print( answer)
        elif func_name == "endswith":
            answer = text.endswith(word)
            print( answer)
        elif func_name == "sorted":
            answer = sorted(word)
            print( answer)


    elif func_name in func_dict.get("other_method"):
        #["Palindrom", "casefold", "sort"]}
        if func_name == "Palindrom":
            answer = "Palindrom"
            print( answer)
        elif func_name == "casefold":
            #ss = "ß".casefold()
            casefold_demo = "Straße"
            answer = casefold_demo.casefold()
            print( answer)
        elif func_name == "sort":
            answer = f"sort kein String Method"
    return answer, zeichen

def user_input():

    # Benutzerantwort
    valid_input = False
    invalid_input = 0
    while not valid_input:
        user_answer = input("Deine Antwort: ")
        try:
            user_answer = int(user_answer)
            valid_input = True
            return user_answer
        except ValueError:
            invalid_input += 1
            if invalid_input < 3:
                print(f"❌ Ungültige Eingabe. du hast noch {3 - invalid_input} Versuche ")
            else:
                print(f"❌ Programm wird beendet")
                return exit(0)
    return None


def run_string(progress = None):
    method = get_method()
    text, word, liter = text_generator()
    set_question(method, text, word, liter)
    antwort, zeichen = string_quiz(method,text, word,liter)
    options = generate_options(antwort)
    for i, opt in enumerate(options, start=1):
        print(f"{i}. {opt}")
    right_index = options.index(antwort)+1
    user = user_input()
    if user is not None:
        if user == right_index:
            print("True")
        else :
            print("False")
    if progress:
        progress.add_attempt(
            module_name="string",
            question="frage nicht vorhanden",  # hier müssen wir math_quiz den text zurückgeben
            user_answer=user,
            correct_answer=antwort
        )

if __name__ == "__main__":

    run_string()


