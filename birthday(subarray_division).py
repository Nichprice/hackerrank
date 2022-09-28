def birthday(s, d, m):
    total = 0
    if m == 1:
        for n in range(0, len(s)):
            newArr = []
            length = 0
            while length < m:
                newArr.append(s[n])
                length += 1
                n += 1
                if len(newArr) == m and sum(newArr) == d:
                    total += 1
    else:
        for n in range(0, (len(s) - m + 1)):
            newArr = []
            length = 0
            while length < m:
                newArr.append(s[n])
                length += 1
                n += 1
                if len(newArr) == m and sum(newArr) == d:
                    total += 1
    return total