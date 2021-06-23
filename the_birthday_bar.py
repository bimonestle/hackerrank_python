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