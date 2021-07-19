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