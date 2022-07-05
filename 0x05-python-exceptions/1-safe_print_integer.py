#!/usr/bin/python3
""" Prints an integer with "{:d}".format().

Returns: True if value has been correctly printed i.e value is an integer
        Otherwise, returns False
    You have to use try: / except:
"""


def safe_print_integer(value):
    try:
        print("{:d}".format(value))
    except (ValueError, TypeError):
        return False
    else:
        return True
