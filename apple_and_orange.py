# The function accepts following parameters:
#  1. INTEGER s
#  2. INTEGER t
#  3. INTEGER a
#  4. INTEGER b
#  5. INTEGER_ARRAY apples
#  6. INTEGER_ARRAY oranges
#

def countApplesAndOranges(s, t, a, b, apples, oranges):
    # Write your code here
    appleHouse = list()
    for apple in apples:
        d = apple + a
        if d >= s and d <= t:
            appleHouse.append(d)
    
    orangeHouse = list()
    for orange in oranges:
        d = orange + b
        if d <= t and d >= s:
            orangeHouse.append(d)
            
    print(len(appleHouse))
    print(len(orangeHouse))