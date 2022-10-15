def breakingRecords(scores):
    # Write your code here
    big = []
    small = []
    bigsmall = []
    big.append(scores[0])
    small.append(scores[0])
    for n in range (1, len(scores)):
        if scores[n] > max(big):
            big.append(scores[n])
        elif scores[n] < min(small):
            small.append(scores[n])
    bigsmall.append(len(big) - 1)
    bigsmall.append(len(small) - 1)
    return bigsmall