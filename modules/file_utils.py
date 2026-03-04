
import json
import csv

def read_json(file_path):
    with open(file_path, "rt") as f:
        return json.load(f)

def write_json(file_path, data):
    with open(file_path, "wt") as f:
        json.dump(data, f, indent=4)

def read_csv(file_path):
    with open(file_path, "rt", newline="") as f:
        reader = csv.reader(f)
        return list(reader)

def write_csv(file_path, data):
    with open(file_path, "wt", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(data)
