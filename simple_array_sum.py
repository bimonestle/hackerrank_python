# Given an array of integers, find the sum of its elements.
# For example, ar = [1, 2, 3], it will return 6

# FUNCTION DESCRIPTION
# Complete the 'simpleArraySum' function in the editor below.
# It must return the sum of the array elements as an integer.

# INPUT FORMAT
# The first input int n, denoting the size of the array
# The second input contains n space-separated integers
# representing the array's elements.
# 6
# 1 2 3 4 10 11

# CONSTRAINTS
# 0 < n, arr[n] ≤ 1000

# OUTPUT FORMAT
# Print the sum of the array's element as a single integer.
# 31

# EXPLANATION
# Print the sum array's elements 1 + 2 + 3 + 4 + 10 + 11 = 31

import math
import os
import random
import re
import sys

# The function is expected to return an INTEGER
# The function accepts INTEGER_ARRAY as parameter
arrNumbs = list()
sizeArr = int(input('Enter array size: '))
numbers = input("Enter numbers: ")
arrNumbs = numbers.split()

def simpleArraySum(ar):
    total = 0
    for numb in ar:
        numb = int(numb)
        total += numb
    print(total)
    return total

simpleArraySum(arrNumbs)