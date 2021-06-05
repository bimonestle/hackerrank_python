# You are choreographing a circus show with various animals.
# For one act, you are given two kangaroos on a number line
# ready to jump in the positive direction (i.e, toward positive infinity).

# The first kangaroo starts at location x1 and moves at a rate of v1 meters per jump.
# The second kangaroo starts at location x2 and moves at a rate of v2 meters per jump.

# You have to figure out a way to get both kangaroos at the
# same location at the same time as part of the show.
# If it is possible, return YES, otherwise return NO.

# After one jump, they are both at x = 3,
# (x1 + v1 = 2 + 1, x2 + v2 = 1 + 2), so the answer is YES.
# int x1: starting position kangaroo 1
# int v1: jump distance for kangaroo 1
# int x2: starting position kangaroo 2
# int v2: jump distance for kangaroo 2

# 0 3 4 2
# YES

# 0 2 5 3
# NO

def kangaroo(x1, v1, x2, v2):
    # Write your code here
    if v2 >= v1:
        return 'NO'
    
    # We just need to solve the equation
    # x1 + y * v1 = x2 + y * v2
    # x1 - x2 + y * v1 = y * v2
    # (x1 - x2) + y * v1 * -y * v2
    # (x1 - x2) + y(v1 - v2)
    # (x1 - x2) = -y(v1 - v2)
    # (x1 - x2) * -1 = -y(v1 - v2) * -1
    # (x2 - x1) = y(v2 - v1)
    # y is the number of jumps
    # Hence, Relative distance divided by relative velocity
    # shouldn't have any remainder. The kangaroo who is starting
    # behind will only be able to catchup with the ahead kangaroo
    # if their relative distance equals or is completely divisible
    # by their relative velocity. Only then they both can reach a Point of Convergence.
    if (x2-x1) % (v2-v1) == 0:
        return 'YES'
    return 'NO'
