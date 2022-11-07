from collections import Counter

def happyLadybugs(b):
    # Write your code here
    bugs = Counter(b)
    for i, j in bugs.items():
        if i != '_' and j == 1:
            return 'NO'

    if bugs['_'] > 0:
        return 'YES'
    else:
        pair = 0
        for i in range(len(b) - 1):
            if b[i] == b[i + 1]:
                pair += 1
            elif pair > 0:
                pair = 0
            else:
                return 'NO'
        return 'YES'
