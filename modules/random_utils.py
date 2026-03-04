import random


class MyRandomFunktionen:
    @staticmethod
    def random_float():
        """Gibt eine Zufallszahl zwischen 0.0 und 1.0 zurück"""
        return random.random()

    @staticmethod
    def random_int(min_val, max_val):
        """Gibt eine Zufallszahl zwischen min_val und max_val zurück (inklusive)"""
        return random.randint(min_val, max_val)

    @staticmethod
    def random_choice(seq):
        """Wählt ein zufälliges Element aus einer Liste"""
        return random.choice(seq)

    @staticmethod
    def random_sample(seq, k):
        """Wählt k eindeutige Elemente aus einer Liste"""
        return random.sample(seq, k)

    @staticmethod
    def shuffle_list(seq):
        """Mischt die Liste in-place"""
        random.shuffle(seq)
        return seq

    @staticmethod
    def uniform_random(min_val, max_val):
        """Float-Zufall zwischen min_val und max_val"""
        return random.uniform(min_val, max_val)

    @staticmethod
    def set_seed(seed_val):
        """Initialisiert den Zufallsgenerator für reproduzierbare Ergebnisse"""
        random.seed(seed_val)

random_funktionen = [["random()","random()","Gibt eine Zufallszahl zwischen 0.0 und 1.0 zurück"],
                     ["randint()","randint(min_val, max_val)","Gibt eine Zufallszahl zwischen min_val und max_val zurück (inklusive)"],
                     ["choice()","choice(seq)","Wählt ein zufälliges Element aus einer Liste" ],
                     ["sample()","sample(seq, k)","Wählt k eindeutige Elemente aus einer Liste" ],
                     ["shuffle()","shuffle(seq)","Mischt die Liste in-place" ],
                     ["uniform()","uniform(min_val, max_val)", "Float-Zufall zwischen min_val und max_val"],
                     ["seed()","seed(seed_val)", "Initialisiert den Zufallsgenerator für reproduzierbare Ergebnisse"]]

func_map = {
    "random()": MyRandomFunktionen.random_float,
    "randint()": lambda: MyRandomFunktionen.random_int(1, 10),
    "choice()": lambda: MyRandomFunktionen.random_choice(["Python", "AI", "Datenbanken"]),
    "sample()": lambda: MyRandomFunktionen.random_sample(["Python", "AI", "Datenbanken"], 2),
    "shuffle()": lambda: MyRandomFunktionen.shuffle_list(["Python", "AI", "Datenbanken"]),
    "uniform()": lambda: MyRandomFunktionen.uniform_random(1, 10),
    "seed()": lambda: MyRandomFunktionen.set_seed(40)
}

def random_quiz():
    questions = random_funktionen.copy()
    random.shuffle(questions)
    get_method = random.choice(questions)
    name, call_str, desc = get_method
    question_text = f"description: {desc}"
    print(question_text)
    correct = name
    other_answers = [f[0] for f in random_funktionen if f != get_method]
    wrong = random.sample(other_answers, 3)
    options = wrong + [correct]
    random.shuffle(options)
    for i, opt in enumerate(options):
        print(f"  {i + 1}. {opt}")
    test_result = func_map[name]()
    example = f"Testlauf: random.{call_str}, {test_result}, Typ: {type(test_result)}"
    #print(f"Testlauf: random.{call_str}, {test_result}, Typ: {type(test_result)}")

    return question_text,correct, options, example

def user_input():
    while True:
        ans = input("Deine Antwort (1-4), or 'q' to quit: ")

        if ans.upper() == "Q":
            return None

        if ans.isdigit():
            ans = int(ans)
            if 1 <= ans <= 4:
                return ans

        print("Bitte eine Zahl von 1-4 oder 'q' eingeben.")


def run_random(progress):
    print("=== Info zum Test ===")
    print(f'Angemommen: seq = ["Python", "AI", "Datenbanken"], k= 2')
    print(f"\t\t    min_val = 1, max_val = 10, seed = 40")
    print("-"*50)
    question_text,correct, options, example = random_quiz()
    ans = user_input()

    if ans is None:
        print("Quiz beendet.")
        return
    ans_text = options[ans - 1]
    if ans_text == correct:
        print("richtig")
    else:
        print("false")
    print(example)
    progress.add_attempt(
        module_name="random",
        question=question_text,
        user_answer=ans_text,
        correct_answer=correct
    )




if __name__ == "__main__":
    def run_random():
        print("=== Info zum Test ===")
        print(f'Angemommen: seq = ["Python", "AI", "Datenbanken"], k= 2')
        print(f"\t\t    min_val = 1, max_val = 10, seed = 40")
        print("-" * 50)
        question_text, correct, options, example = random_quiz()
        ans = user_input()

        if ans is None:
            print("Quiz beendet.")
            return
        ans_text = options[ans - 1]
        if ans_text == correct:
            print("richtig")
        else:
            print("false")
        print(example)
    while True:
        run_random()