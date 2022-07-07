#!/bin/python
import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input().strip())

# Hackerrank python challenge if-else
if (n < 1 or n > 100):
    exit()

else:
    # if it's odd
    if (n % 2 != 0):
        print("Weird")
    if (n % 2 == 0):
        if (n >= 2 and n <= 5):
            print("Not Weird")
            
        if (n >= 6 and n <= 20):
            print("Weird")
        
        if (n > 20):
            print("Not Weird")
    
