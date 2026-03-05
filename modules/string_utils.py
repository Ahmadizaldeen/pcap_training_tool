from faker import Faker
from random import shuffle, choice
fake = Faker()

class StringMethods:
    @staticmethod
    def find_substring(s, sub):
        return s.find(sub)

    # map, filter, text analyzer
    @staticmethod
    def is_upper_case(s):
        return s.isupper()
    @staticmethod
    def join_words(self, words, sep=" "):
        return sep.join(words)
    @staticmethod
    def split_string(s, sep=None):
        return s.split(sep)
    @staticmethod
    def doppelte_erkennen(words):
        duplicates=set([w for w in words if words.count(w)>1])
        return f"Doppelte Wörter:",duplicates if duplicates else"Keine"
    @staticmethod
    def len_str(sting):
        word_lengths= {w:len(w)for w in sting}
        print("Länge:",word_lengths)
string_funktionen = [["split()","String → Liste"],
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




def string_quiz ():
    str_func = string_funktionen.copy()
    shuffle(str_func)
    get_func = choice(str_func)
    func_name, desc = get_func
    #print(get_func)



    text = fake.text(70)
    words = [w.strip(".,'") for w in text.split()]
    litter = list(words[0] + words[1])
    question_text = f"what is the output from : {func_name}({words[2]})"
    print(question_text)
    print(list(map(lambda word: word.title(), words[0:3])))
    #print(list(map(str.title, words)))




    return text,words,litter


def run_string():
    text, words, litter = string_quiz()
    print(text)

if __name__ == "__main__":
    run_string()
    ue ="ß".casefold()
    print(ue)