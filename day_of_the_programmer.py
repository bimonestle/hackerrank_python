def leapYear(year):
    if year >= 1700 and year <= 1917:
        if year % 4 == 0:
            return 244
    if year > 1917:
        if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
            return 244
        elif year == 1918:
            return 243 - 13
    return 243

def dayOfProgrammer(year):
    date = 256 - leapYear(year)
    print("%d.09.%d" % (date, year))
    return str(date) + '.09.' + str(year)

dayOfProgrammer(2017)