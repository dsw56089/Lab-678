# main.py
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("filepath")
args = parser.parse_args()
print(f"Plik wejściowy: {args.filepath}")
