# main.py
import argparse
import json

parser = argparse.ArgumentParser()
parser.add_argument("filepath")
args = parser.parse_args()
print(f"Plik wejściowy: {args.filepath}")
with open(args.filepath, 'r') as f:
    try:
        data = json.load(f)
        print("Poprawnie wczytano JSON.")
    except json.JSONDecodeError as e:
        print(f"zła składnia JSON: {e}")
