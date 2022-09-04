from distutils.log import warn


def saveThePrisoner(prisoners, candies, start):
    remaining_steps = candies % prisoners
    
    # Get the warned_prisoner from
    # the remeaining_steps condition
    if remaining_steps == 0:
        if start == 1:
          warned_prisoner = prisoners
        else:
          warned_prisoner = start - 1
    else:
        warned_prisoner = start - 1 + remaining_steps

    # Loop to eliminate the remaining value
    # of the warned_prisoner calculation
    while warned_prisoner > prisoners:
        warned_prisoner = warned_prisoner % prisoners
    
    return warned_prisoner