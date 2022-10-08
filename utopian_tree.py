def utopianTree(n):
    # Write your code here
    h = []
    h.append(1)
    for period in range(1, n + 1):
        if period % 2 != 0:
            h.append(h[period - 1] * 2)
        elif period % 2 == 0:
            h.append(h[period - 1] + 1)
    return h[n]