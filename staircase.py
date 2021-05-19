# STAIRCASE
# This is a staircase n = 4
#    o
#   oo
#  ooo
# oooo

def staircase(n):
    for i in range(n):
        for j in range(n):
            if j >= (n-i-1):
                print('#', end='')
            else:
                print(' ', end='')
        print('')