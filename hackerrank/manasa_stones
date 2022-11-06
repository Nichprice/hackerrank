def stones(n, a, b):
    # Write your code here
    tots = []
    n = n - 1
    for i in range(n + 1):
        if i == 0:
            tots.append(((n - i) * a) + (i * b))
        elif i > 0 and tots[len(tots) - 1] != ((n - i) * a) + (i * b):
            tots.append(((n - i) * a) + (i * b))
    return sorted(tots)