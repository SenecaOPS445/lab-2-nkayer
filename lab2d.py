#!/usr/bin/env python3

import sys

# Check if exactly two arguments are provided (name and age)
if len(sys.argv) != 3:
    # If not, print usage message and exit
    print(f"Usage: {sys.argv[0]} name age")
    sys.exit()

# Assign command line arguments to name and age
name = sys.argv[1]
age = sys.argv[2]

# Output the formatted message
print(f"Hi {name}, you are {age} years old.")

