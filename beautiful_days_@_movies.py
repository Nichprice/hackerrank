def beautifulDays(i, j, k):
    # Write your code here
    counter = 0
    for n in range(i, (j + 1)):
        rev = int(str(n)[::-1])
        if abs(n - rev) % k == 0:
            counter += 1
    return counter