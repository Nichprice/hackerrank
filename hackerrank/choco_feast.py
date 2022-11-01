

def chocolateFeast(n, c, m):
    # Write your code here
    choco = n // c
    wraps = choco
    while wraps >= m:
        choco += wraps // m
        wraps = (wraps // m) + (wraps % m)
    return choco
