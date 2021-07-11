def bonAppetit(bill: list, k: int, b: int):
    bill.pop(k)

    annaBill = sum(bill) / 2
    result = int(b - annaBill)

    if annaBill == b:
        print('Bon Appetit')
    else:
        print(result)