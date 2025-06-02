# main.py
import argparse
import json

parser = argparse.ArgumentParser()
parser.add_argument("filepath")
args = parser.parse_args()
print(f"Plik wejściowy: {args.filepath}")

try:
    with open(args.filepath, 'r') as f:
        data = json.load(f)
        print("wczytano JSON.")
except json.JSONDecodeError as e:
    print(f"Błąd: {e}")
    exit(1)
except FileNotFoundError:
    print("Plik nie został znaleziony.")
    exit(1)
with open('output.json', 'w') as f:
    json.dump(data, f, indent=4)
    print("Zapisano dane do output.json")
