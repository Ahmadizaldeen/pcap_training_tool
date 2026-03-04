
import platform
import random


from .exceptions_utils import MethodNotImplementiertError


def get_system_info():
    return {
        "system": platform.system(),
        "machine": platform.machine(),
        "processor": platform.processor(),
        "python_version": platform.python_version(),
        "implementation": platform.python_implementation(),
        "platform" : platform.platform(),
        "version" : platform.version(),
        "python_version_tuple" : platform.python_version_tuple(),
        "uname": platform.uname(),
        "node": platform.node(),
        "architecture": platform.architecture()
    }

platform_methods = [
    "platform",
    "machine",
    "processor",
    "system",
    "version",
    "python_implementation",
    "python_version_tuple",
    "python_version",
    "uname",
    "node",
    "architecture"
]
def platform_quiz():
    func_name = random.choice(platform_methods)
    question_text = f"Was gibt die Funktion {func_name} zurück?"


    func_map = {
        "platform": platform.platform,
        "system": platform.system,
        "machine": platform.machine,
        "processor": platform.processor,
        "python_version": platform.python_version,
        "python_implementation": platform.python_implementation,
        "version": platform.version,
        "python_version_tuple": platform.python_version_tuple,
        "uname": platform.uname,
        "node": platform.node,
        "architecture": platform.architecture
    }

    if func_name not in func_map:
        raise MethodNotImplementiertError(f"{func_name} nicht implementiert")

    output = func_map[func_name]()
    return question_text, func_name, output
def user_input():
    for i, name in enumerate(platform_methods, start=1):
        print(f"{i}. {name}")

    choice = input("Select die richtige Methode: ")

    try:
        choice = int(choice)
        if 1 <= choice <= len(platform_methods):
            return platform_methods[choice - 1]
    except ValueError:
        pass

    print("Ungültige Eingabe")
    return None
def run_platform(progress):
    print(get_system_info())
    question_text, func_name, output = platform_quiz()

    print("\nWelcher Methode gehört folgendes Output?")
    print("----------------------------------------")
    print(output)
    print("----------------------------------------")

    user_choice = user_input()

    if user_choice == func_name:
        print("Richtig ✅")
    else:
        print(f"Falsch ❌. Richtig war: {func_name}")

    progress.add_attempt(
        module_name="platform",
        question=f"Output: {output}",
        user_answer=user_choice,
        correct_answer=func_name
    )



if __name__ == "__main__":
    pass
    #run_platform()