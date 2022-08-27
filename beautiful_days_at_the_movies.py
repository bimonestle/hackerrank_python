# Lily likes to play games with integers.
# She has created a new game where she determines
# the difference between a number and its reverse.
# For instance, given the number 12, its reverse is 21.
# Their difference is 9.
# The number 120 reversed is 21, and their difference is 99.

# She decides to apply her game to decision making.
# She will look at a numbered range of days and will only go to a movie on a beautiful day.

# Given a range of numbered days, [i...j] and a number 'k',
# determine the number of days in the range that are beautiful.
# Beautiful numbers are defined as numbers where |i - reverse(i)|
# is evenly divisible by 'k'. If a day's value is a beautiful number,
# it is a beautiful day. Return the number of beautiful days in the range.

# Example
# 20 23 6
# Lily may go to the movies on days 20, 21, 22, and 23.
# We perform the following calculations to determine which days are beautiful:
# 
# Day 20 is beautiful because the following whole number:
# (|20 - 02|) / 6 = 3
# 
# Day 21 is not beautiful because the following doesn't evaluate to the whole number:
# (|21 - 12|) / 6 = 1,5
# 
# Day 22 is beautiful because the following whole number:
# (|22 - 22|) / 6 = 0
# 
# Day 23 is not beautiful because the following doesn't evaluate to the whole number:
# (|23 - 32|) / 6 = 1,5
# 
# Only 2 days (20 & 22) in this interval are beautiful.
# Thus, we print 2 as our answer.

def reverseDay(day: int):
    reverse = ''
    strDay = str(day)
    
    # loop backwards the day
    # to make it in reversed order
    for idx in range(len(strDay)-1, -1, -1):
        
        # concatenate the reversed number
        reverse += strDay[idx]
    return int(reverse)
        
def beautifulDays(startDay, endDay, divisor):
    beautiful = 0
    for day in range(startDay, (endDay+1)):
        difference = abs(day - reverseDay(day))
        
        if difference % divisor == 0:
            beautiful += 1
    return beautiful