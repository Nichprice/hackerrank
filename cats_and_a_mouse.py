def catAndMouse(x, y, z):
    x_dist = abs(x - z)
    y_dist = abs(y - z)
    if x_dist < y_dist:
        return 'Cat A'
    elif y_dist < x_dist:
        return 'Cat B'
    elif x_dist == y_dist:
        return 'Mouse C'