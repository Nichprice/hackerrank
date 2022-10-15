def libraryFine(d1, m1, y1, d2, m2, y2):
    # Write your code here
    if y1 > y2:
        return ((y1 - y2) * 10000)
    elif y1 == y2:
        if m1 > m2:
            return((m1 - m2) * 500)
        if m1 == m2:
            if d1 > d2:
                return((d1 - d2) * 15)
            else:
                return 0
        if m1 < m2:
            return 0
    elif y1 < y2:
        return 0
