def sockMerchant(n: int, ar: int) -> int:
    res = list()
    for el in ar:
        if el not in res:
            res.append(el)

    pair = 0
    for el in res:
        val = ar.count(el)
        result = int(val / 2)
        pair += result

    print(pair)
    return pair

n = 9
arr = [10, 20, 20, 10, 10, 30, 50, 10, 20]
n = 10
arr = [1, 1, 3, 1, 2, 1, 3, 3, 3, 3]
sockMerchant(n, arr)