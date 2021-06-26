# Given an array of integers and a positive integer 'k', determine the number of '(i, j)' pairs
# where 'i < j' and 'ar[i] + ar[j]' is divisible by 'k'.

# Example
# ar = [1, 2, 3, 4, 5, 6]
# k = 5
# Three pairs meet the criteria [1, 4], [2, 3] & [4, 6]

def divisibleSumPairs(n: int, k: int, ar: list) -> int:
    count = 0
    for i in range(n-1):
        for j in range(i+1, n):
            sumPair = ar[i] + ar[j]
            if sumPair % k == 0:
                # if ar[i] < ar[j]:
                #     count += 1
                count += 1
    return count