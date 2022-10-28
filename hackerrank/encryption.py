import math

def encryption(s):
    # Write your code here
    sq_rt = len(s) ** .5
    col = math.ceil(sq_rt)
    ans = []
    for num in range(col):
        ans.append([])
    for i in range(len(s)):
        ans[i % col].append(s[i])
    for num in range(col):
        ans[num] = (''.join(ans[num]))
    return ' '.join(ans)