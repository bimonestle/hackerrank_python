# Given an array of integers, calculate the ratios
# of its elements that are positive, negative, and zero.
# Print the decimal value of each fraction on a new line
# with 6 places after the decimal.

# example:
# arr = [1, 1, 0, -1, -1]
# There are n = 5 elements,
# 2 positives, 2/5 == 0.400000
# 2 negatives, 2/5 == 0.400000
# 1 zero, 1/5 == 0.200000

# Print
# Print the ratios of positive, negative and zero values in the array.
# Each value should be printed on a separate line with 6 digits after the decimal.
# The function should not return a value.

def plusMinus(arr):
    # Write your code here
    pos = 0
    zero = 0
    neg = 0
    for numb in arr:
        if numb < 0:
            neg += 1
        elif numb > 0:
            pos += 1
        else:
            zero += 1
    
    results = [pos, neg, zero]
    for val in results:
        result = val / len(arr)
        print('%.6f' % result)