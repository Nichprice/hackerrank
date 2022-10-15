n = 6
p = 2

def pageCount(n, p):
    # Write your code here
    turns = []
    from_start = p - 1
    if from_start == 0:
        turns.append(0)
    elif from_start % 2 == 0:
        turns.append(from_start / 2)
    elif from_start % 2 != 0:
        adjusted = from_start + 1
        turns.append(adjusted / 2)
    from_end = n - p
    if n % 2 == 0:
        if from_end < 1:
            turns.append(0)
        elif from_end == 1:
            turns.append(1)
        elif from_end > 1:
            if from_end % 2 == 0:
                turns.append(from_end / 2)
            else:
                turns.append((from_end - 1) / 2)
    elif n % 2 != 0:
        if from_end <= 1:
            turns.append(0)
        elif from_end > 1:
            if from_end % 2 == 0:
                turns.append(from_end / 2)
            else:
                turns.append((from_end - 1) / 2)
    return int(min(turns))


pageCount(n, p)