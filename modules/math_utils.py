
import math
import random # use my random Mod
from .exceptions_utils import MethodNotImplementiertError # . ist sehr wichtig , dazu muss Modules ein Package sein (ohne . start von andere Modul nicht möglich) relativer Import.

math_methods_all = [
    "ceil", "floor", "trunc", "factorial", "sqrt", "hypot",
    "fabs", "pow", "exp", "log", "log10", "log2",
    "cos", "sin", "tan", "acos", "asin", "atan", "atan2",
    "degrees", "radians", "gcd", "lcm", "prod", "comb", "perm", "dist"
]
pcap_math_methods = [  # modulo?
    "ceil", "floor", "trunc", "factorial", "sqrt","pow", "hypotenuse","log", "log10", "log2"
]
nicht_implementiert=["fabs", "prod", "comb", "perm","hypot", "dist","gcd", "lcm","atan2","cos","sin","tan","acos","asin","atan","degrees","radians"]

def math_quiz():#
    correct = None
    func_name = random.choice(pcap_math_methods)# zufällige Funktion auswählen
    question_text = f"Funktion: {func_name}"  # Default, später verbessern
    print(f"Math-Funktion: {func_name}")
    # Eingabewerte abhängig von der Funktion generieren

    if func_name in ["ceil", "floor", "trunc", "sqrt", "exp"]:
        x = random.uniform(1, 20) # float
        question_text = f"{func_name}({x:.2f})"
        print(f"Angenommen: x = {x:.2f}")
        if func_name == "ceil":
            correct = math.ceil(x)
        elif func_name == "floor":
            correct = math.floor(x)
        elif func_name == "trunc":
            correct = math.trunc(x)
        elif func_name == "sqrt":
            correct = math.sqrt(x)
        elif func_name == "exp":
            correct = math.exp(x)

    elif func_name == "factorial": #int
        x = random.randint(1, 10)
        correct = math.factorial(x)
        print(f"Angenommen: n = {x}")
    elif  func_name == "hypotenuse":
        x = random.randint(1,10)
        y = random.randint(1,10)
        correct = math.hypot(x, y)
        print(f"Angenommen: x = {x}, y = {y}")
    else:
        raise MethodNotImplementiertError(f"{func_name} nicht implementiert")

    if correct is not None:
        correct =round(correct,2)
    return correct, question_text


def user_input():
    # Benutzerantwort
    valid_input = False
    invalid_input = 0
    while not valid_input:
        user_answer = input("Deine Antwort: ")
        try:
            user_answer = float(user_answer)
            valid_input = True
            return user_answer
        except ValueError:
            invalid_input += 1
            if invalid_input < 3:
                print(f"❌ Ungültige Eingabe. du hast noch {3-invalid_input} Versuche ")
            else:
                print(f"❌ Programm wird beendet")
                return exit(0)
    return None


def run_math(progress):
    try:
        correct, question_text = math_quiz()
    except MethodNotImplementiertError as e:
        print(f"⚠ Fehler: {e}")
        return
    if correct is None:
        return
    answer = user_input()
    if abs(answer - correct)<= 0.01:
        print("Richtig ✅")
    else :
        print(f"Falsch ❌. Richtig: {correct}")
        # progress ist jetzt ein ProgressManager-Objekt
    progress.add_attempt(
        module_name="math",
        question=question_text,  # hier müssen wir math_quiz den text zurückgeben
        user_answer=answer,
        correct_answer=correct
    )



# Testlauf
if __name__ == "__main__":
    # print(math_quiz())
    # print(user_input())
    #print(lambda x :math_quiz())
    #progress = ProgressManager()
    #run_math(progress)
    print()

