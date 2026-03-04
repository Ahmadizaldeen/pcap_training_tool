
import json
import os


class ProgressManager:
    def __init__(self, file_path):
        self.file_path = file_path
        self.progress = {}
        self.load_progress()

    def load_progress(self):
        """Lädt progress.json oder initialisiert leeren Fortschritt"""
        if os.path.exists(self.file_path):
            try:
                with open(self.file_path, "r", encoding="utf-8") as f:
                    self.progress = json.load(f)
            except (PermissionError, json.JSONDecodeError):
                print("⚠️ Fehler beim Laden der Fortschrittsdatei. Neuer Fortschritt wird erstellt.")
                self.progress = {}
        else:
            self.progress = {}

        # Alte Integer-Werte migrieren
        for key, value in list(self.progress.items()):
            if isinstance(value, int):
                self.progress[key] = {
                    "attempts": value,
                    "correct": value,
                    "wrong": 0,
                    "last_10": []
                }

    def save_progress(self):
        """Speichert die Fortschrittsdatei"""
        try:
            with open(self.file_path, "w", encoding="utf-8") as f:
                json.dump(self.progress, f, indent=4, ensure_ascii=False)
        except PermissionError:
            print("⚠️ Keine Schreibberechtigung für progress.json")

    def add_attempt(self, module_name, question, user_answer, correct_answer):
        """Speichert einen neuen Versuch für ein Modul"""
        self.progress.setdefault(module_name, {
            "attempts": 0,
            "correct": 0,
            "wrong": 0,
            "last_10": []
        })

        self.progress[module_name]["attempts"] += 1

        is_correct = (user_answer == correct_answer)
        if is_correct:
            self.progress[module_name]["correct"] += 1
        else:
            self.progress[module_name]["wrong"] += 1

        entry = {
            "question": question,
            "user": user_answer,
            "correct": correct_answer,
            "result": is_correct
        }

        self.progress[module_name]["last_10"].append(entry)
        # Nur die letzten 10 behalten
        self.progress[module_name]["last_10"] = self.progress[module_name]["last_10"][-10:]

        self.save_progress()

    def get_module_progress(self, module_name):
        """Gibt den Fortschritt eines Moduls zurück"""
        return self.progress.get(module_name, {
            "attempts": 0,
            "correct": 0,
            "wrong": 0,
            "last_10": []
        })

    def get_overall_progress(self):
        """Gibt alle Module zurück"""
        return self.progress

    def get_module_names(self):
        return list(self.progress.keys())


    def get_module_progress_any(self, module_name):
        module_names = self.get_module_names()
        print(module_names)
        choise = input("module auswählen")
        if choise in module_names:
            for modul in module_names:
                if modul == choise:
                    module_name = self.get_module_progress(choise)
        else:
            print("Exception , modul not found")

        """Gibt den Fortschritt eines Moduls zurück"""
        return self.progress.get(module_name, {
            "attempts": 0,
            "correct": 0,
            "wrong": 0,
            "last_10": []
        })

