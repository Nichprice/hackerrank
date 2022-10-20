def jumpingOnClouds(c):
    # Write your code here
    cloud = 0
    j_c = 0
    while cloud < len(c) - 1:
        if cloud == len(c) - 2:
            cloud += 1
            j_c += 1
        elif c[cloud + 2] == 0:
            cloud += 2
            j_c += 1
        elif c[cloud + 1] == 0:
            cloud += 1
            j_c += 1
    return j_c
