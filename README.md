# PCAP Training Tool

> 🇩🇪 Deutsch | 🇬🇧 [English below](#english)

---

## 🇩🇪 Deutsch

### Über das Projekt

Dieses Tool habe ich entwickelt, um mich auf die **PCAP – Certified Associate in Python Programming** Prüfung von Python Institute vorzubereiten – und sie erfolgreich zu bestehen.

Es ist ein interaktives CLI-Quiz, das alle relevanten Prüfungsthemen abdeckt. Statt statischer Lernkarten werden Fragen dynamisch generiert, sodass jede Übungssitzung anders ist.

---

### Features

- **12 Quiz-Module** zu allen PCAP-relevanten Themen
- **Dynamische Fragen** mit der `faker`-Bibliothek – keine zwei Sitzungen sind gleich
- **Fortschrittsspeicherung** via JSON – Ergebnisse werden zwischen Sitzungen gespeichert
- **Statistik-Ansicht** – zeigt Trefferquote pro Modul
- **Multiple-Choice-Format** – prüfungsnah

---

### Abgedeckte Themen

| # | Modul | Themen |
|---|-------|--------|
| 1 | Math | `math`-Modul: `ceil`, `floor`, `sqrt`, `factorial`, `log` |
| 2 | Plattform | `platform`-Modul: Systeminformationen |
| 3 | Random | `random`-Modul: `choice`, `randint`, `shuffle` |
| 4 | String | String-Methoden: `split`, `join`, `find`, `replace`, `upper` u.v.m. |
| 5 | Generatoren | `yield`, `next()`, `StopIteration`, Generator-Expressions, Iterator-Protokoll |
| 6 | Filter / Map / Zip | `filter()`, `map()`, `zip()`, lazy evaluation |
| 7 | OOP | Klassen, Vererbung, Komposition, `@classmethod`, `@staticmethod` |
| 8 | Lambda & Closures | Lambda-Funktionen, Closures, Higher-Order Functions |
| 9 | Datenstrukturen | List, Dict, Set, Tuple – Operationen und Comprehensions |
| 10 | File Utils | JSON lesen/schreiben, Dateioperationen |
| 11 | Decorators | `@decorator`, `@property`, MRO, `functools.wraps` |
| 12 | Fortschritt | Statistik aller Module |

---

### Installation

```bash
# Repository klonen
git clone https://github.com/Ahmadizaldeen/pcap_training_tool.git
cd pcap_training_tool

# Abhängigkeit installieren
pip install faker

# Tool starten
python main.py
```

---

### Projektstruktur

```
pcap_training_tool/
├── main.py               # Einstiegspunkt & Menü
├── modules/
│   ├── progress_utils.py # ProgressManager – Speicherung & Statistik
│   ├── math_utils.py
│   ├── string_utils.py
│   ├── generator.py
│   ├── filter.py
│   ├── oop_examples.py
│   ├── lambda_closures.py
│   ├── data_structures.py
│   ├── decorators_oop.py
│   ├── file_utils.py
│   ├── platform_utils.py
│   └── cli_utils.py
└── progress.json         # Wird automatisch erstellt
```

---

### Technologien

- **Python 3.11+**
- **faker** – dynamische Testdaten
- **json** – Fortschrittsspeicherung
- **Git** – Feature-Branch-Workflow mit Pull Requests

---

---

## English <a name="english"></a>

### About

I built this tool to prepare for — and pass — the **PCAP – Certified Associate in Python Programming** exam by Python Institute.

It is an interactive CLI quiz covering all relevant exam topics. Questions are generated dynamically so every practice session feels different.

---

### Features

- **12 quiz modules** covering all PCAP exam topics
- **Dynamic questions** using the `faker` library — no two sessions are the same
- **Progress tracking** via JSON — results persist between sessions
- **Statistics view** — shows success rate per module
- **Multiple-choice format** — close to the real exam style

---

### Topics Covered

| # | Module | Topics |
|---|--------|--------|
| 1 | Math | `math` module: `ceil`, `floor`, `sqrt`, `factorial`, `log` |
| 2 | Platform | `platform` module: system information |
| 3 | Random | `random` module: `choice`, `randint`, `shuffle` |
| 4 | String | String methods: `split`, `join`, `find`, `replace`, `upper` and more |
| 5 | Generators | `yield`, `next()`, `StopIteration`, generator expressions, iterator protocol |
| 6 | Filter / Map / Zip | `filter()`, `map()`, `zip()`, lazy evaluation |
| 7 | OOP | Classes, inheritance, composition, `@classmethod`, `@staticmethod` |
| 8 | Lambda & Closures | Lambda functions, closures, higher-order functions |
| 9 | Data Structures | List, Dict, Set, Tuple — operations and comprehensions |
| 10 | File Utils | JSON read/write, file operations |
| 11 | Decorators | `@decorator`, `@property`, MRO, `functools.wraps` |
| 12 | Progress | Statistics across all modules |

---

### Installation

```bash
# Clone the repository
git clone https://github.com/Ahmadizaldeen/pcap_training_tool.git
cd pcap_training_tool

# Install dependency
pip install faker

# Run the tool
python main.py
```

---

### Project Structure

```
pcap_training_tool/
├── main.py               # Entry point & menu
├── modules/
│   ├── progress_utils.py # ProgressManager – saving & statistics
│   ├── math_utils.py
│   ├── string_utils.py
│   ├── generator.py
│   ├── filter.py
│   ├── oop_examples.py
│   ├── lambda_closures.py
│   ├── data_structures.py
│   ├── decorators_oop.py
│   ├── file_utils.py
│   ├── platform_utils.py
│   └── cli_utils.py
└── progress.json         # Auto-generated on first run
```

---

### Tech Stack

- **Python 3.11+**
- **faker** – dynamic test data generation
- **json** – progress persistence
- **Git** – feature branch workflow with pull requests

---

### Author

Ahmad Izaldeen — [GitHub](https://github.com/Ahmadizaldeen)
