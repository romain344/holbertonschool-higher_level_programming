#!/usr/bin/python3
def safe_print_integer(value):
    try:
        print("{:d".formay(value))
        return true
    except (ValueError, TypeError):
        return False
