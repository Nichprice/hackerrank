def countingValleys(steps, path):
    path = list(path)
    # Write your code here
    altitude = 0
    map = []
    valleys = 0
    for step in path:
        if step == 'U':
            altitude += 1
            map.append(altitude)
        elif step == 'D':
            altitude -= 1
            map.append(altitude)
    for n in range(0, len(map)):
        if map[n] == 0:
            if map[n-1] < 0:
                valleys += 1
    return valleys

