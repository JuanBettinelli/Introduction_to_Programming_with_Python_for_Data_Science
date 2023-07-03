#! /bin/python
from ast import Match, match_case
import sys

"""
Test script to run with specific python version
"""

print("Will this run?")
print('.')
print('.')
http_status = 404
match http_status:
    case 404:
        print("Error 404: Not found.")
    case _:
        print("Internet has lost its mind.")
print('.')
print('.')
print("test 3 successful")
