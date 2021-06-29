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
    sortSeen = sorted(seen.items(), key=lambda x:x[1], reverse=True)
    print(sortSeen)
    result = 0
    tempVal = 0
    for i in sortSeen:
        if i[1] > tempVal:
            print('key:', i[0])
            tempVal = i[1]
            result = i[0]
        elif i[1] == tempVal:
            print('key:', i[0])
            tempVal = i[1]
            result = i[0]
        else:
            break
    return result

arr = [2, 4, 3, 2, 3, 1, 2, 1, 3, 3]
# arr = [1, 2, 3, 4, 5, 4, 3, 2, 1, 3, 4]
migratoryBirds(arr)