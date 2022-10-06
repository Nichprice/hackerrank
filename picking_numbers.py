def pickingNumbers(a):
    # Write your code here
    low =  min(a)
    high = max(a)
    a.sort()
    leng = []
    for n in range(low, (high + 1)):
        counter = 0
        for num in a:
            if num == n or num == n + 1:
                counter += 1
                leng.append(counter)
    return max(leng)