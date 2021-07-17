# There is a large pile of socks that must be paired by color.
# Given an array of integers representing the color of each sock,
# determine how many pairs of socks with matching colors there are.

# Example
# n = 7
# ar = [1, 2, 1, 2, 1, 3, 2]
# There is one pair of color 1 and 2.
# There are three odd socks left, one of each color.
# The number of pairs is 2.

# Sample input 1
# ar = [10, 20, 20, 10, 10, 30, 50, 10, 20]
# output = 3 (2 pairs of color 1, 1 pair color 2)

def sockMerchant(n: int, ar: int) -> int:
    res = list()

    # for each element of 'ar' array which is not in 'res' array,
    # append it to the 'res' array.
    for el in ar:
        if el not in res:
            res.append(el)

    # print(res) # debugging
    pair = 0

    # for each element of 'res' array,
    # count the amount of color 'el' inside 'ar' array.
    # divide each sum amount of color by 2 and
    # add variable 'pair' by the result of the sum amount of color
    for el in res:
        val = ar.count(el)
        result = int(val / 2)
        pair += result

    print(pair)
    return pair

n = 9
arr = [10, 20, 20, 10, 10, 30, 50, 10, 20]
n = 10
arr = [1, 1, 3, 1, 2, 1, 3, 3, 3, 3]
sockMerchant(n, arr)