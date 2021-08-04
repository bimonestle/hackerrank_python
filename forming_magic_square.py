def formingMagicSquare(s: list) -> int:
    # find if there are duplicates in each list
    # the sum for each element must be 15
    print(s)
    one_Dim_Arr = list()
    for lstA in s:
        for lstB in lstA:
            # print(lstB)
            one_Dim_Arr.append(lstB)

    print(one_Dim_Arr)
    # for idx, el in enumerate(one_Dim_Arr):
    #     if one_Dim_Arr[idx] == el:
    #         print(True)

s = [[5, 3, 4], [1, 5, 8], [6, 4, 2]]

formingMagicSquare(s)