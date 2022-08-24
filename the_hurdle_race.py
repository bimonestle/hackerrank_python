# A video player plays a game in which
# the character competes in a hurdle race.
# Hurdles are of varying heights,
# and the characters have a maximum height they can jump.
# There is a magic potion they can take that will increase
# their maximum jump height by 1 unit for each dose.
# 
# How many doses of the potion must the character take
# to be able to jump all of the hurdles?
# If the character can already clear all of the hurdles, return 0.

# Example
# height = [1,2,3,3,2]
# k = 1
# The character can jump 1 unit high initially
# and must take 3 - 1 = 2 doses of potion
# to be able to jump all of the hurdles.

# Example
# height = [1,6,3,5,2]
# k = 4
# Dan's character can jump a maximum of 4 units,
# but the tallest hurdle has a height of h: 6
# To be able to jump all the hurdles, Dan must drink 6 - 4 = 2 doses.

# Example
# height = [2,5,4,5,2]
# k = 7
# Dan's character can jump a maximum of 7 units,
# but the tallest hurdle has a height of h: 5
# To be able to jump all the hurdles, Dan must drink 0 doses.
# Since it can jump at 7 unit high and high enough to cross the hurdles.

def hurdleRace(k, height):
    # Write your code here
    dose = 0
    max_height = max(height)
    if k <= max_height:
        dose = max_height - k
    
    return dose