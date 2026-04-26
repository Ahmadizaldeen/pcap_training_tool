"""
filter_utils.py - PCAP Quiz-Modul: filter(), map(), zip()
Themen: filter(), map(), zip(), lambda mit built-ins, lazy evaluation
"""

import random
from faker import Faker

fake = Faker()


# ---------------------------------------------------------------------------
# Fragen-Pool
# ---------------------------------------------------------------------------

def _question_filter_basic():
    """filter() mit einfacher Lambda-Bedingung auf Zahlen."""
    numbers = random.sample(range(1, 20), 8)
    threshold = random.choice([5, 7, 10, 12])
    result = list(filter(lambda x: x > threshold, numbers))
    question = (
        f"numbers = {numbers}\n"
        f"result = list(filter(lambda x: x > {threshold}, numbers))\n"
        f"Was ist len(result)?"
    )
    return question, len(result), [len(result), len(result) + 1, len(result) - 1, len(numbers)]


def _question_filter_even():
    """filter() gerade Zahlen herausfiltern."""
    numbers = random.sample(range(1, 30), 10)
    result = list(filter(lambda x: x % 2 == 0, numbers))
    question = (
        f"numbers = {numbers}\n"
        f"result = list(filter(lambda x: x % 2 == 0, numbers))\n"
        f"Was ist len(result)?"
    )
    return question, len(result), [len(result), len(result) + 2, len(numbers), 0]


def _question_filter_none():
    """filter(None, ...) entfernt falsy-Werte."""
    pool = [0, 1, "", "hello", None, 42, False, True, [], [1]]
    sample = random.sample(pool, 6)
    result = list(filter(None, sample))
    question = (
        f"data = {sample}\n"
        f"result = list(filter(None, data))\n"
        f"Was ist len(result)?"
    )
    return question, len(result), [len(result), len(result) + 1, len(sample), 0]


def _question_map_double():
    """map() Werte verdoppeln."""
    numbers = [random.randint(1, 10) for _ in range(5)]
    result = list(map(lambda x: x * 2, numbers))
    idx = random.randint(0, 4)
    question = (
        f"numbers = {numbers}\n"
        f"result = list(map(lambda x: x * 2, numbers))\n"
        f"Was ist result[{idx}]?"
    )
    correct = result[idx]
    distractors = [correct, correct + 1, correct - 1, numbers[idx]]
    return question, correct, distractors


def _question_map_str():
    """map() auf Strings - len()."""
    words = [fake.word() for _ in range(5)]
    result = list(map(len, words))
    idx = random.randint(0, 4)
    question = (
        f"words = {words}\n"
        f"result = list(map(len, words))\n"
        f"Was ist result[{idx}]?"
    )
    correct = result[idx]
    distractors = [correct, correct + 1, correct - 1, len(words)]
    return question, correct, distractors


def _question_map_type():
    """map() gibt ein Iterator-Objekt zuruck, nicht eine Liste."""
    question = (
        "numbers = [1, 2, 3]\n"
        "result = map(lambda x: x * 2, numbers)\n"
        "Was ist type(result).__name__?"
    )
    correct = "map"
    distractors = ["map", "list", "filter", "generator"]
    return question, correct, distractors


def _question_zip_basic():
    """zip() kombiniert zwei Listen."""
    a = [random.randint(1, 5) for _ in range(4)]
    b = [fake.word()[:3] for _ in range(4)]
    idx = random.randint(0, 3)
    result = list(zip(a, b))
    question = (
        f"a = {a}\n"
        f"b = {b}\n"
        f"result = list(zip(a, b))\n"
        f"Was ist result[{idx}]?"
    )
    correct = str(result[idx])
    distractors = [str(result[idx]), str(result[idx - 1]), str((b[idx], a[idx])), str(a[idx])]
    return question, correct, distractors


def _question_zip_unequal():
    """zip() stoppt beim kurzeren Iterable."""
    a = list(range(1, 6))
    b = list(range(1, 4))
    result = list(zip(a, b))
    question = (
        f"a = {a}\n"
        f"b = {b}\n"
        f"result = list(zip(a, b))\n"
        f"Was ist len(result)?"
    )
    correct = len(result)
    distractors = [len(result), len(a), len(b) + 1, len(a) + len(b)]
    return question, correct, distractors


def _question_filter_type():
    """filter() gibt ein Iterator-Objekt zuruck."""
    question = (
        "numbers = [1, 2, 3, 4, 5]\n"
        "result = filter(lambda x: x > 2, numbers)\n"
        "Was ist type(result).__name__?"
    )
    correct = "filter"
    distractors = ["filter", "list", "bool", "map"]
    return question, correct, distractors


def _question_map_upper():
    """map() mit str.upper."""
    words = [fake.word().lower() for _ in range(4)]
    result = list(map(str.upper, words))
    idx = random.randint(0, 3)
    question = (
        f"words = {words}\n"
        f"result = list(map(str.upper, words))\n"
        f"Was ist result[{idx}]?"
    )
    correct = result[idx]
    distractors = [result[idx], words[idx], result[idx].lower(), result[idx].title()]
    return question, correct, distractors


# ---------------------------------------------------------------------------
# Quiz-Engine
# ---------------------------------------------------------------------------

QUESTIONS = [
    _question_filter_basic,
    _question_filter_even,
    _question_filter_none,
    _question_map_double,
    _question_map_str,
    _question_map_type,
    _question_zip_basic,
    _question_zip_unequal,
    _question_filter_type,
    _question_map_upper,
]


def _make_options(correct, raw_distractors):
    """
    Baut 4 einzigartige Antwortoptionen als Strings.

    Returns:
        tuple: (optionen_liste, 1-basierter Index der richtigen Antwort)
    """
    correct_str = str(correct)
    seen = set()
    options = []
    for d in raw_distractors:
        s = str(d)
        if s not in seen:
            seen.add(s)
            options.append(s)
        if len(options) == 4:
            break

    if correct_str not in options:
        options[0] = correct_str

    random.shuffle(options)
    return options, options.index(correct_str) + 1


def _user_choice(num_options):
    """Liest eine gultige Zahl 1..num_options vom Nutzer ein."""
    while True:
        raw = input(f"Deine Antwort (1-{num_options}, 0 = Abbrechen): ").strip()
        if raw == "0":
            return None
        try:
            choice = int(raw)
            if 1 <= choice <= num_options:
                return choice
        except ValueError:
            pass
        print(f"  Bitte eine Zahl zwischen 1 und {num_options} eingeben.")


def run_filter(progress):
    """
    Startet eine zufaellige filter()/map()/zip()-Quizfrage.

    Args:
        progress (ProgressManager): Instanz fuer Fortschrittsspeicherung.
    """
    question_fn = random.choice(QUESTIONS)
    question_text, correct, raw_distractors = question_fn()

    print("\n--- filter / map / zip Quiz ---")
    print(question_text)
    print()

    options, correct_idx = _make_options(correct, raw_distractors)

    for i, opt in enumerate(options, start=1):
        print(f"  {i}. {opt}")

    user = _user_choice(len(options))
    if user is None:
        print("Abgebrochen.")
        return

    if user == correct_idx:
        print("Richtig ✅")
    else:
        print(f"Falsch ❌  Richtig: {correct_idx}. {str(correct)}")

    progress.add_attempt(
        module_name="filter_map_zip",
        question=question_text.splitlines()[0],
        user_answer=user,
        correct_answer=correct_idx,
    )


# ---------------------------------------------------------------------------
if __name__ == "__main__":
    from modules.progress_utils import ProgressManager
    p = ProgressManager("progress.json")
    run_filter(p)