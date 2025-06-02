#!/usr/bin/python3
"""Script that adds all command line arguments to a JSON list file."""

import sys
from save_to_json_file import save_to_json_file
from load_from_json_file import load_from_json_file

def main():
    filename = "add_item.json"
    try:
        items = load_from_json_file(filename)
    except Exception:
        items = []
        
    args = sys.argv[1:]

    items.extend(args)
    save_to_json_file(items, filename)

if __name__ == "__main__":
    main()