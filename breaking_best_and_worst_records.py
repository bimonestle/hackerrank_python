def breakingRecords(scores):
    # Write your code here
    maxCount = 0
    minCount = 0
    newScore = dict()
    result = list()
    for idx, score in enumerate(scores):
        if idx == 0:
            newScore['Highest'] = score
            newScore['Lowest'] = score
        if score > newScore['Highest']:
            maxCount += 1
            newScore['Highest'] = score
        elif score < newScore['Lowest']:
            minCount += 1
            newScore['Lowest'] = score
    result.append(maxCount)
    result.append(minCount)
    
    return result