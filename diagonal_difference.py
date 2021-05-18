# Given a square matrix, calculate the absolute difference between the sums of its diagonals.
# For example, the square matrix arr is shown below:
# 1 2 3
# 4 5 6
# 9 8 9

# The left-right diagonal is 15. Because 1 + 5 + 9
# The right-left diagonal is 17. Because 3 + 5 + 9
# Their absolute difference is |15-17| = 2

# 11 2 4
# 4 5 6
# 10 8 -12
# Their absolute difference is |4-19| = 15

def diagonalDifference(arr):
    # diagonal value left-to-right
    xA = 0

    # diagonal value right-to-left
    xB = 0
    
    for idxA, arrNum in enumerate(arr):
        for idxB, numb in enumerate(arrNum):
            if idxA == idxB:
                xA += numb
            if ((len(arrNum) - 1) - idxA) == idxB:
                xB += numb

    result = xA - xB
    if result < 0:
        result *= -1

    return result