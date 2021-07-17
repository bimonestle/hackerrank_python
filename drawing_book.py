def pageCount(n, p):
    # Write your code here
    leftOpen = int(p/2)

    if n % 2 == 0:
        n += 1
    rightOpen = int((n-p)/2)
    
    result = 0
    if leftOpen < rightOpen:
        result = leftOpen
        print(leftOpen)
    else:
        result = rightOpen
        print(rightOpen)
    
    return result