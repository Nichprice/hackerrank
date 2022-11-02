def flatlandSpaceStations(n, c):
    c.sort()
    ans = []
    for i in range(len(c)):
        temp = []
        if len(c) == 1:
            temp.append(abs(c[i] - 0))
            temp.append(abs(c[i] - (n - 1)))
        else:
            if i == 0:
                temp.append(abs(c[i]- 0))
                temp.append((abs(c[i] - c[i + 1])) // 2)
            elif i == len(c) - 1:
                temp.append(abs(c[i] - (n - 1)))
                temp.append(abs(c[i] - c[i-1]) // 2)
            else:
                temp.append(abs(c[i] - c[i + 1]) // 2)
                temp.append(abs(c[i] - c[i - 1]) // 2)
        print(temp)
        ans.append(max(temp))
    return max(ans)  
