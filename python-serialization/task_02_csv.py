#!/usr/bin/python3
"""inilisalise le code"""


import csv
import json

def convert_csv_to_json(csv_filename):
    """define la fonction"""
    try:
        with open(csv_filename, mode='r', newline='') as csv_file:
            reader = csv.DictReader(csv_file)
            data = [row for row in reader]

        with open('data.json', mode='w') as json_file:
            json.dump(data, json_file, indent=4)

        return True
    except Exception as e:
        print(f"Error: {e}")
        return False
