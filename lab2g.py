#!/usr/bin/env python3

# Author: [Your Full Name]
# Author ID: [Your Seneca ID]
# Date Created: 2025/01/23

import sys

# Check if a command-line argument is provided
if len(sys.argv) > 1:
    timer = int(sys.argv[1])  # Use the argument as the timer value
else:
    timer = 3  # Default value if no argument is provided

# While loop that repeats until timer equals 0
while timer > 0:
    print(timer)
    timer -= 1  # Decrement the timer by 1 each iteration

# Once the countdown is done, print "blast off!"
print("blast off!")

