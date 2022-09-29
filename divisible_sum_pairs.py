def divisibleSumPairs(n, k, ar):
    # Write your code here
    pairs = 0
    for i in range(0, n):
        j = i + 1
        for j in range(j, n):
            if (ar[i] + ar[j]) % k == 0:
                pairs += 1
    return(pairs)