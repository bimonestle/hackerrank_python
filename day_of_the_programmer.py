def isLeapYear(year):
    if year >= 1700 and year <= 1917:
        if year % 4 == 0:
            return True
    if year > 1917:
        if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
            return True
    return False

def dayOfProgrammer(year):
    if isLeapYear(year):
        return '12.09.' + str(year)
    return '13.09.' + str(year)