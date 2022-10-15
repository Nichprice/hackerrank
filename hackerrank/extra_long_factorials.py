def extraLongFactorials(n):
    # Write your code here
    tot = 1
    for num in range(1, n + 1):
        tot = tot * num
    print(tot)