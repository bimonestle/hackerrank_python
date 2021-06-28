def migratoryBirds(arr):
    seen = dict()
    count = 1
    arr.sort(reverse=True)
    print('arr:', arr)
    for i in range(len(arr)):
        try:
            if arr[i] == arr[i+1]:
                count += 1
                seen[arr[i]] = count
            else:
                count = 1
        except:
            break
    
    print(seen)
    keyList = list(seen.keys())
    valList = list(seen.values())
    result = 0
    tempVal = 0
    print('key list:',keyList)
    print('val list:',valList)
    for i in range(len(valList)):
        if valList[i] > tempVal:
            print('key:', keyList[i])
            tempVal = valList[i]
            result = keyList[i]
        elif valList[i] == tempVal:
            print('key:', keyList[i])
            tempVal = valList[i]
            result = keyList[i]
        else:
            break
        print('loop result:', result)
    print('result:', result)
    return result

arr = [2, 4, 3, 2, 3, 1, 2, 1, 3, 3]
arr = [1, 2, 3, 4, 5, 4, 3, 2, 1, 3, 4]
migratoryBirds(arr)