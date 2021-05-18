# Alice and Bob each created one problem for HackerRank.
# A reviewer rates the two challenges, awarding points on a scale
# from 1 to 100 for three categories: problem clarity, originality, and difficulty.

# The rating for Alice's challenge is the triplet a = (a[0], a[1], a[2]),
# and the rating for Bob's challenge is the triplet b = (b[0], b[1], b[2]).

# The task is to find their comparison points by comparing
# a[0] with b[0],
# a[1] with b[1], and
# a[2] with b[2].

# If a[i] > b[i], then Alice is awarded 1 point.
# If a[i] < b[i], then Bob is awarded 1 point.
# If a[i] = b[i], then neither person receives a point.

# Comparison points is the total points a person earned.
# Given a and b, determine their respective comparison points.

# Sample input 0:
# 5 6 7
# 3 6 10
# Sample Output 0
# 1 1

# Sample Input 1
# 17 28 30
# 99 16 8
# Sample Output 1
# 2 1

# a = Integer Array A
# b = Integer Array B
def compareTriplets(a, b):
    result = list()
    Alice = 0
    Bob = 0

    for idxA, numA in enumerate(a):
        for idxB, numB in enumerate(b):
            if idxA == idxB:
                if numA > numB:
                    Alice += 1
                if numB > numA:
                    Bob += 1

    result.append(Alice)
    result.append(Bob)
    
    return result