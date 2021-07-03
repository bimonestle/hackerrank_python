# Given an array of bird sightings where every element represents a bird type id,
# determine the id of the most frequently sighted type. If more than 1 type has been
# spotted that maximum amount, return the smallest of their ids.

# Example:
# arr = [1, 1, 2, 2, 3]

# There are two of each types 1 and 2, and one sighting of 3.
# Pick the lower of the two types seen twice: type 1.

# Constraints
# 5 ≤ n ≤ 2*10^5
# It is guaranteed that each type is 1, 2, 3, 4 or 5.

def migratoryBirds(arr):
    seen = dict()
    count = 1

    # Sort the array descendingly and add counter if it matches the condition.
    # The condition is if the index value the same as the next index, add counter
    # Then assign the value to the dictionary key.
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

    # Sort the assigned object based on the value. Sort it descendingly.
    sortSeen = sorted(seen.items(), key=lambda x:x[1], reverse=True)
    print(sortSeen)
    result = 0
    tempVal = 0

    # tuples[0] = key
    # tuples[1] = value
    # if the value is greater or equal than temporary value,
    # assign temporary value with the value and
    # assign the result with the key
    # else, break the loop.
    for i in sortSeen:
        if i[1] >= tempVal:
            print('key:', i[0])
            tempVal = i[1]
            result = i[0]
        else:
            break
    return result

arr = [2, 4, 3, 2, 3, 1, 2, 1, 3, 3]
# arr = [1, 2, 3, 4, 5, 4, 3, 2, 1, 3, 4]
migratoryBirds(arr)