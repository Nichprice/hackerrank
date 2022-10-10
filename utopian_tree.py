def utopianTree(n):
    # Write your code here
    h = []
    for period in range(0, n + 1):
        if period == 0:
            h.append(1)
        elif period % 2 != 0:
            h.append(h[period - 1] * 2)
        elif period % 2 == 0:
            h.append(h[period - 1] + 1)
    return h[n]