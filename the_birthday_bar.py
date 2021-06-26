# Two children, Lily and Ron, want to share a chocolate bar. Each of the squares has an integer on it.
# Lily decides to share a contiguous segment of the bar selected such that:
# • The length of the segment matches Ron's birth month, and,
# • The sum of the integers on the squares is equal to his birth day.
# Determine how many ways she can divide the chocolate.

# Example
# s = [2, 2, 1, 3, 2]
# d = 4
# m = 2
# Lily wants to find segments summing to Ron's birth day, d = 4 with a length equalling his birth month, m = 2.
# In this case, there are two segments meeting her criteria: [2, 2] and [1, 3].

# s = [1, 2, 1, 3, 2]
# d = 3
# m = 2
# [1, 2], [2, 1]

# s = [1, 1, 1, 1, 1, 1]
# d = 3
# m = 2
# none

# s = [4]
# d = 4
# m = 1
# [4]

def birthday(s: list, d: int, m: int) -> int:
    count = 0

    if m == 1:
        count = 1
    
    for i in range((len(s) - 1)):
        if sum(s[i:i+m]) == d:
            count += 1
    
    print(count)
    return count

# arr = [1, 2, 1, 3, 2]
# date = 3
# month = 2
# # length 5
# # 2

arr = [2, 5, 1, 3, 4, 4, 3, 5, 1, 1, 2, 1, 4, 1, 3, 3, 4, 2, 1]
date = 18
month = 7
# length 19
# 3

# arr = [1, 1, 1, 1, 1, 1]
# date = 3
# month = 2
# # length 6
# # 0

# arr = [2, 2, 2, 1, 3, 2, 2, 3, 3, 1, 4, 1, 3, 2, 2, 1, 2, 2, 4, 2, 2, 3, 5, 3, 4, 3, 2, 1, 4, 5, 4]
# date = 10
# month = 4
# # length 31
# # 7
birthday(arr,date,month)