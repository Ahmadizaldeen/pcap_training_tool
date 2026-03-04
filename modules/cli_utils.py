#cli_utils.py

def show_module_statistics(progress, module_name):#Anzeige für EIN Modul
    data = progress.get_module_progress(module_name)

    attempts = data["attempts"]
    correct = data["correct"]
    wrong = data["wrong"]

    percentage = 0
    if attempts > 0:
        percentage = (correct / attempts) * 100

    print("\n==============================")
    print(f"Statistik für Modul: {module_name}")
    print("------------------------------")
    print(f"Versuche : {attempts}")
    print(f"Richtig  : {correct}")
    print(f"Falsch   : {wrong}")
    print(f"Quote    : {percentage:.2f}%")
    print("==============================")

def show_all_statistics(progress):
    all_data = progress.get_overall_progress()

    print("\n######## Gesamtstatistik ########")

    for module_name, data in all_data.items():
        attempts = data["attempts"]
        correct = data["correct"]

        percentage = 0
        if attempts > 0:
            percentage = (correct / attempts) * 100

        print(f"\nModul: {module_name}")
        print(f"  Versuche: {attempts}")
        print(f"  Richtig : {correct}")
        print(f"  Quote   : {percentage:.2f}%")

def run_statistics(progress):
    modules = ["all", "math", "platform", "random"]

    for i, name in enumerate(modules, start=1):
        print(f"{i}. {name}")

    choice = input("Select to show: ")

    try:
        index = int(choice) - 1
        if modules[index] == "all":
            show_all_statistics(progress)
        else:
            show_module_statistics(progress, modules[index])
    except (ValueError, IndexError):
        print("Nicht verfügbar")


if __name__ == "__main__":
    ...