def formingMagicSquare(s: list) -> int:
    for idx, lstA in enumerate(s):
        if sum(lstA) == 15:
            continue