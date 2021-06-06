from functools import reduce

def gcd(a: int, b: int) -> int:
    while a % b != 0:
        a, b = b, a % b
    return b
def gcd_list(lst: list) -> int:
    return reduce(gcd, lst)

def lcm(a: int, b: int) -> int:
    return a * b // gcd(a, b)
def lcm_list(lst: list) -> int:
    return reduce(lcm, lst)

def evenly_divides(number: int, divisor: int) -> bool:
    return number % divisor == 0

def getTotalX(a: list, b: list) -> int:
    # Find LCM of all integers of a
    lcmValue = lcm_list(a)

    # Find GCD of all integers of b
    gcdValue = gcd_list(b)

    # Count the number of multiple LCM that
    # evenly divides the GCD
    count = 0
    multipleOfLCM = lcmValue
    while multipleOfLCM <= gcdValue:
        if evenly_divides(gcdValue, multipleOfLCM):
            count += 1
        multipleOfLCM += lcmValue
        
    print(count)
    return count

a = [2, 4]
b = [16, 32, 96]
getTotalX(a, b)