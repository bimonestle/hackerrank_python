def migratoryBirds(arr):
    seen = dict()
    count = 1
    arr.sort(reverse=True)

    for i in range(len(arr)):
        try:
            if arr[i] == arr[i+1]:
                count += 1
                seen[arr[i]] = count
            else:
                count = 1
        except:
            break