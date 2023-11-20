#!/usr/bin/python3

import sys

def safe_function(fct, *args):
    try:
        my_var = fct(*args)
        return my_var
    except Exception as e:
        print("Exception: {}".format(e), file=sys.stderr)
        return None
