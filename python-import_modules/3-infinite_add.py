#!/usr/bin/python3
from sys import argv

if __name__ == '__main__':
    total = 0
    for number in range(1, len(argv)):
        number = int(argv[number])
        total += number
    print(total)
