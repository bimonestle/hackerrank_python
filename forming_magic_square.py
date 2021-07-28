def formingMagicSquare(s: list) -> int:
    # find if there are duplicates in each list
    # the sum for each element must be 15
    for idx, lstA in enumerate(s):
        if sum(lstA) == 15:
            continue