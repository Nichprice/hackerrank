def fairRations(B):
    # Write your code here
    odds = 0
    for num in B:
        if num % 2 != 0:
            odds += 1
    breads = 0
    if odds % 2 != 0:
        return 'NO'
    else:
        for i in range(len(B) - 1):
            if B[i] % 2 != 0:
                B[i] = B[i] + 1
                B[i + 1] = B[i + 1] + 1
                breads += 2
    return str(breads)