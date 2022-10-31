def howManyGames(p, d, m, s):
    # Return the number of games you can buy
    paid = []
    counter = 0
    while sum(paid) < s:
        current = p - (counter * d)
        if current > m:
            counter += 1
            paid.append(current)
        else:
            counter += 1
            paid.append(m)
    if sum(paid) == s:
        return counter
    else:
        return counter - 1