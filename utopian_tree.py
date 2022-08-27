# The utopian tree goes through 2 cycles of growth every year.
# Each spring, it doubles in height. Each summer, its height increases by 1 meter

# A utopian tree sapling the height of 1 meter 
# is planted on the onset of spring.
# How tall will the tree be after 'n' growth cycles?

# Example 1
# If the number growth cycles is n = 5,
# the calculation is as follows:
# Period    Height
# 0         1
# 1         2
# 2         3
# 3         6
# 4         7
# 5         14

# Example 2
# Period    Height
# 0         1
# 1         2
# 4         7

def utopianTree(n):
    if n <= 0:
        n += 1
    elif n % 2 != 0:
        n = utopianTree(n-1) * 2
    else:
        n = utopianTree(n-1) + 1
        
    return n