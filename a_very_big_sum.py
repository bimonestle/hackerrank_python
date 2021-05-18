# In this challenge, you are required to calculate and
# print the sum of the elements in an array, keeping in mind
# that some of those integers may be quite large.

# FUNCTION DESCRIPTION
# It must return the sum of all array elements.
# aVeryBigSum has the following parameter(s):
# int ar[n]: an array of integers.

# RETURN
# long: the sum of all array elements

# SAMPLE INPUT
# 5
# 1000000001 1000000002 1000000003 1000000004 1000000005
# OUTPUT
# 5000000015

def aVeryBigSum(ar):
    total = 0
    for numb in ar:
        total += numb
    
    return total