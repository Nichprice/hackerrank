def minimumDistances(a):
    # Write your code here
    ans = []
    for i in range(len(a) - 1):
        for j in range(i + 1, len(a)):
            if a[i] == a[j]:
                ans.append(j - i)
    if len(ans) > 0:
        return min(ans)
    else:
        return -1