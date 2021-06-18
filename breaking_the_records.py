def breakingRecords(scores):
    # Write your code here
    maxCount = 0
    minCount = 0
    result = list()
    for idx, score in enumerate(scores):
        if idx == 0:
            highest = score
            lowest = score
            
        if score > highest:
            maxCount += 1
            highest = score
        elif score < lowest:
            minCount += 1
            lowest = score
    result.append(maxCount)
    result.append(minCount)
    
    return result