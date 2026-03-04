from faker import Faker

fake = Faker()

def find_substring(s, sub):
    return s.find(sub)

# map, filter, text analyzer

def is_upper_case(s):
    return s.isupper()

def join_words(words, sep=" "):
    return sep.join(words)

def split_string(s, sep=None):
    return s.split(sep)


def string_quiz ():
    text = fake.text(70)
    words = text.split()
    litter = list(words[0] + words[1])
    

    return text,words,litter


def run_string():
    text, words, litter = string_quiz()
    print(text)

if __name__ == "__main__":
    run_string()