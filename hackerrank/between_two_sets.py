def getTotalX(a, b):
    # Write your code here
    begin = max(a)
    end = min(b)
    ans = 0
    for integers in range(begin, (end + 1)):
        if all(integers % num == 0 for num in a) and all(num % integers == 0 for num in b):
            ans += 1
    return ans