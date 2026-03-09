
import json
import random
from modules.progress_utils import ProgressManager
from modules.math_utils import run_math
from modules.platform_utils import run_platform
from modules.cli_utils import run_statistics
from modules.random_utils import run_random
from modules.string_utils import run_string
from modules import (
    io_utils, exceptions_utils, oop_examples, lambda_closures,
    data_structures, file_utils, decorators_oop
)


def migrate_progress(progress):
    for key, value in progress.items():
        if isinstance(value, int):
            progress[key] = {
                "attempts": value,
                "correct": value,
                "wrong": 0,
                "last_10": []
            }
    return progress

PROGRESS_FILE = "progress.json"

def load_progress():
    try:
        with open(PROGRESS_FILE, "rt") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def save_progress(progress):
    try:
        with open(PROGRESS_FILE, "w") as f:
            json.dump(progress, f, indent=4)
    except PermissionError:
        print("⚠️ Keine Schreibberechtigung für progress.json")



def string_quiz(progress):
    sentences = ["Python ist super","Ich liebe Programmieren"]
    s = random.choice(sentences)
    print(f"String: '{s}'")
    sub = input("Gib Substring ein: ")
    idx = string_utils.find_substring(s,sub)
    if idx != -1:
        print(f"Gefunden ✅ an Position {idx}")
        progress["string"] = progress.get("string",0)+1



def exceptions_quiz(progress):
    a = random.randint(1,10)
    b = random.choice([0,1,2])
    print(f"{a} / {b} versuchen")
    try:
        exceptions_utils.safe_divide(a,b)
    except exceptions_utils.CustomError:
        print("CustomError ✅")
        progress["exceptions"] = progress.get("exceptions",0)+1

def oop_quiz(progress):
    car = oop_examples.Car("Audi",4,"A4")
    print("Auto Beschreibung:", car.description())
    progress["oop"] = progress.get("oop",0)+1

def lambda_closure_quiz(progress):
    x = random.randint(1,10)
    square = lambda n: n*n
    print(f"{x}^2 =", lambda_closures.apply_func(x,square))
    closure = lambda_closures.closure_example(f"Test {x}")
    print(closure())
    progress["lambda_closure"] = progress.get("lambda_closure",0)+1

def data_structures_quiz(progress):
    print("--- Data Structures Quiz ---")
    data_structures.list_ops()
    data_structures.dict_ops()
    data_structures.set_ops()
    data_structures.tuple_ops()
    progress["data_structures"] = progress.get("data_structures",0)+1

def file_utils_quiz(progress):
    sample_json = {"name":"Ahmad","age":22}
    file_utils.write_json("test.json", sample_json)
    loaded = file_utils.read_json("test.json")
    print("Gelesen:", loaded)
    progress["file_utils"] = progress.get("file_utils",0)+1

def decorators_oop_quiz(progress):
    @decorators_oop.my_decorator
    def test_func(x): return x*2
    print("Testfunktion:", test_func(5))
    circle = decorators_oop.Circle(3)
    print("Circle area:", circle.area)
    c = decorators_oop.C()
    c.greet()
    progress["decorators_oop"] = progress.get("decorators_oop",0)+1

def main():
    # progress = load_progress()# json-file , dict
    # progress = migrate_progress(progress)
    progress = ProgressManager(PROGRESS_FILE)
    while True:
        print("\n=== PCAP Trainings-Tool ===")
        print("1.Math 2.Plattform 3.Random 4.Stirng 5.OOP 6.Lambda 7.DataStruct 8.FileUtils 9.Decorators 10.Fortschritt 0.Exit")
        choice = input("Wähle: ")
        if choice=="1": run_math(progress)#  math_quiz(progress)
        elif choice=="2": run_platform(progress)
        elif choice=="3": run_random(progress)
        elif choice=="4": run_string(progress)
        elif choice=="5": oop_quiz(progress)
        elif choice=="6": lambda_closure_quiz(progress)
        elif choice=="7": data_structures_quiz(progress)
        elif choice=="8": file_utils_quiz(progress)
        elif choice=="9": decorators_oop_quiz(progress)
        elif choice=="10":run_statistics(progress)
        elif choice=="0": break
        progress.save_progress()
        print("Fortschritt gespeichert ✅")

if __name__=="__main__":
    main()
