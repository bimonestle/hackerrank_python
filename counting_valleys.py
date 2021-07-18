def countingValleys(steps: int, path: str) -> int:
    summ = 0
    valleys = 0
    for el in path:
        if el == 'U':
            summ += 1
            if summ == 0:
                valleys += 1
        else:
            summ -= 1

    print(valleys)
    return valleys

countingValleys(8, 'UDDDUDUU')
countingValleys(12, 'DDUUDDUDUUUD')