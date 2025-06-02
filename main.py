import argparse
import json
import yaml
import os
from lxml.etree import ElementTree as ET, parse, tostring, Element
parser = argparse.ArgumentParser()
parser.add_argument("filepath")
parser.add_argument("output")
args = parser.parse_args()


print(f"Plik wejściowy: {args.filepath}")
print(f"Plik wyjściowy: {args.output}")
data = None

extension = os.path.splitext(args.filepath)[1].lower()
extension_output = os.path.splitext(args.output)[1].lower()
try:
    with open(args.filepath, 'r') as f:
        if extension == ".json":
            try:
                data = json.load(f)
                print("Poprawnie wczytano JSON.")
            except json.JSONDecodeError as e:
                print(f"Błąd składni JSON: {e}")
                exit(1)
        elif extension in [".yaml", ".yml"]:
            try:
                data = yaml.safe_load(f)
                print("Poprawnie wczytano YAML.")
            except yaml.YAMLError as e:
                print(f"Błąd składni YAML: {e}")
                exit(1)
        elif extension == ".xml":
            try:
                tree = parse(f)
                root = tree.getroot()
                data = {child.tag: child.text for child in root}
                print("Poprawnie wczytano XML.")
            except Exception as e:
                print(f"Błąd składni XML: {e}")
                exit(1)
        else:
            print("Nieobsługiwane rozszerzenie pliku. Użyj .json, .yaml lub .yml.")
            exit(1)
except FileNotFoundError:
    print("Plik nie został znaleziony.")
    exit(1)
try:
    if extension_output == ".yaml" or extension_output == ".yml":
        with open(args.output, 'w') as f:
            yaml.dump(data, f, default_flow_style=False)
            print("Zapisano dane " + args.output)
    elif extension_output == ".json":
        with open(args.output, 'w') as f:
            json.dump(data, f, indent=4)
            print("Zapisano dane" + args.output)
    elif extension_output == ".xml":
        try:
            root = Element("root")
            for key, value in data.items():
                child = Element(key)
                child.text = value
                root.append(child)
            with open(args.output, 'wb') as f:
                f.write(tostring(root, pretty_print=True, xml_declaration=True, encoding="UTF-8"))
            print("Zapisano dane " + args.output)
        except Exception as e:
            print(f"Błąd podczas zapisu XML: {e}")
            exit(1)
except Exception as e:
    print(f"Błąd podczas zapisu pliku: {e}")
    exit(1)
