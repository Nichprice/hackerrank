def serviceLane(n, cases):
    # Write your code here
    ans = []
    for case in cases:
        i = case[0]
        j = case[1]
        temp = []
        for k in range(i, j + 1):
            temp.append(width[k])
        ans.append(min(temp))
    return ans