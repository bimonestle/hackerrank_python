# A person wants to determine the most expensive computer keyboard and
# USB drive that can be purchased with a give budget. Given price lists
# for keyboards and USB drives and a budget, find the cost to buy them.
# If it is not possible to buy both items, return '-1'.

# Example
# Budget = 60
# Keyboards = [40, 50, 60]
# Drives = [5, 8, 12]
# The person can buy a '40 keyboard + 12 USB drives'
# or a '50 keyboard + 8 USB drives'.
# Choose the latter as the more expensive option
# and return '58'

# Sample 1
# 10 2 3
# 3 1
# 5 2 8
# return 9

# Sample 2
# 5 1 1
# 4
# 5
# return -1

def getMoneySpent(keyboards, drives, b):
    pair = 0
    for keyboard in keyboards:
        for drive in drives:
            summ = keyboard + drive
            # print('keyboard:', keyboard, ", drive:", drive, 'summ:', summ) # debugging
            if summ <= b:
                # print('pair:', pair) # debugging
                if summ > pair:
                    pair = summ
            if pair == 0:
                pair = -1
    
    # print(pair) # debugging
    return pair

keyboards = [40, 50, 60]
drives = [5, 8, 12]
budget = 60
getMoneySpent(keyboards, drives, budget)