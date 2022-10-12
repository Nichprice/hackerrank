def jumpingOnClouds(c, k):
    e = 100
    cloud = 0
    n = len(c)
    notzero = True
    while notzero:
        cloud = (cloud + k) % n
        e -= 1
        if c[cloud] == 1:
            e -= 2
        if cloud == 0:
            notzero = False
    return e
