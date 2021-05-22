# Given a time in 12 hour format, convert it to military hour or 24 hour format.

# Example
# s = 12:00:00AM
# output = 00:00:00
# s = 12:00:00PM
# output = 12:00:00

def timeConversion(s):
    if s[-2:] == 'AM' and s[:2] == '12':
        return '00' + s[2:-2]
    elif s[-2:] == 'AM' or (s[-2:] == 'PM' and s[:2] == '12'):
        return s[:-2]
    else:
        return str(int(s[:2]) + 12) + s[2:-2]