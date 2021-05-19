# Given five positive integers, find the minimum and maximum values
# that can be calculated by summing exactly four of the five integers.
# Then print the respective minimum and maximum values as a single line
# of two space-separated long integers.

# Print
# Print two space-separated integers on one line:
# the minimum sum and the maximum sum of 4 of 5 elements.

# Sample Input
# 1 2 3 4 5
# Sample Output
# 10 14

# Explanation
# The numbers are 1, 2, 3, 4, and 5. Calculate the following sums using four of the five integers:
# Sum everything except 1, the sum is 2 + 3 + 4 + 5 = 14. --> Max Sum
# Sum everything except 2, the sum is 1 + 3 + 4 + 5 = 13.
# Sum everything except 3, the sum is 1 + 2 + 4 + 5 = 12.
# Sum everything except 4, the sum is 1 + 2 + 3 + 5 = 11.
# Sum everything except 5, the sum is 1 + 2 + 3 + 4 = 10. --> Min Sum

def minMaxSum(arr):
    total = 0
    result = list()

    # duplicate the array from the argument
    tempArr = arr.copy()

    for idx, numb in enumerate(arr):

        # remove element based on the iterated index
        tempArr.pop(idx)
        
        # iterate through the (just-removed-element) array
        for num in tempArr:
            total += num
        
        result.append(total)

        # reset the duplicated array and reset the total value
        tempArr = arr.copy()
        total = 0
    
    # sort ascend the 'result' array
    result.sort()
    minSum = result[0]
    maxSum = result[len(arr)-1]

    print(minSum,maxSum)