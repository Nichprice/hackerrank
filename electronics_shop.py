def getMoneySpent(keyboards, drives, b):
    # Write your code here.
    totals = []
    for keyboard in keyboards:
        for drive in drives:
            if keyboard + drive <= b:
                totals.append(keyboard + drive)
    if len(totals) < 1:
        return(-1)
    else:
        return max(totals)