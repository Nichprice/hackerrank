def saveThePrisoner(n, m, s):
    # Write your code here
    rec = (s + m - 1) % n
    ans  = 0
    if rec == 0:
        ans = n
    else:
        ans = rec
    return ans