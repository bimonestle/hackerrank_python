def birthday(s: list, d: int, m: int) -> int:
    count = 0
    calc = 0
    month = m

    for i in range(0, len(s)):
        print('idx', i)
        for j in range(i, len(s)):
            print('jdx', j, s[j])
            if len(s) == 1:
                if s[j] == d:
                    count += 1
                    break
            month -= 1
            print('month:', month)
            if month < 0:
                month = m
                break
            calc += s[j]
            print('calc', calc)
            if calc == d:
                calc = 0
                count += 1
                month = m
                break
    print(count)
    return count

# arr = [1, 2, 1, 3, 2]
# date = 3
# month = 2
# arr = [2, 5, 1, 3, 4, 4, 3, 5, 1, 1, 2, 1, 4, 1, 3, 3, 4, 2, 1]
# date = 18
# month = 7
arr = [1, 1, 1, 1, 1, 1]
date = 3
month = 2
birthday(arr,date,month)