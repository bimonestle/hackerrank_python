# Given an array of integers,
# find the longest subarray where the absolute difference
# between any two elements is less than or equal to 1.

# Example
# a = [1,1,2,2,4,4,5,5,5]
# There are two subarrays meeting the criterion.
# [1,1,2,2]
# [4,4,5,5,5]
# The longest one from those subarrays is
# [4,4,5,5,5] = 5

# Example
# a = [4,6,5,3,3,1]
# Subarrays:
# [3,3,4]
# [4,5]
# [5,6]
# The longest one from those subarrays is
# [3,3,4] = 3

# Example
# a = [1,2,2,3,1,2]
# Subarrays:
# [1,1,2,2,2]
# [2,2,2,3]
# The longest one from those subarrays is
# [1,1,2,2,2] = 5

def pickingNumbers(a):
    sorted_arr = sorted(a)
    long_subarr = list()
    temp_subarr = list()
    count = 0
    # 1,3,3,4,5,6
    for idx, el in enumerate(sorted_arr):
        for jdx, elm in enumerate(sorted_arr):
            # To make the jdx iterate with the same
            # starting point with idx
            jdx += idx
            if jdx > len(sorted_arr)-1:
                continue
            
            # When the absolute difference is 1 or 0,
            # assign it to 'temporary subarray'
            if abs(sorted_arr[idx]-sorted_arr[jdx]) <= 1:
                temp_subarr.append(sorted_arr[jdx])
            else:
                continue
        
        # Compare the length from 'temporary subarray'
        # and 'long subarray'
        if len(temp_subarr) > len(long_subarr):
            long_subarr = list(temp_subarr)
            temp_subarr.clear()
        else:
            temp_subarr.clear()
    return len(long_subarr)