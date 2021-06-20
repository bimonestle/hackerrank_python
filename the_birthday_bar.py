def birthday(s: list, d: int, m: int) -> int:
    count = 0
    calc = s[0]
    month = m - 1

    if len(s) == 1:
        if s[0] == d:
            count += 1

    for i in range(1, len(s)):
        print('idx', i)
        for j in range(i, len(s)):
            print('jdx', j)
            calc += s[j]
            print('month:', month)
            print('calc', calc)
            month -= 1
            if month < 0:
                month = m - 1
                break
            
            if calc == d:
                # calc = s[i]
                count += 1
                # month = m -1
                break
            elif calc > d:
                # calc = s[i]
                # month = m - 1
                break
        calc = s[i]
        month = m - 1
    print(count)
    return count

# arr = [1, 2, 1, 3, 2]
# date = 3
# month = 2
# arr = [2, 5, 1, 3, 4, 4, 3, 5, 1, 1, 2, 1, 4, 1, 3, 3, 4, 2, 1]
# date = 18
# month = 7
# arr = [1, 1, 1, 1, 1, 1]
# date = 3
# month = 2
arr = [2, 2, 2, 1, 3, 2, 2, 3, 3, 1, 4, 1, 3, 2, 2, 1, 2, 2, 4, 2, 2, 3, 5, 3, 4, 3, 2, 1, 4, 5, 4]
date = 10
month = 4
birthday(arr,date,month)