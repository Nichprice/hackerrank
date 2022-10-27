def kaprekarNumbers(p, q):
    # Write your code here
    ans = []
    for num in range(p, q + 1):
        sq = str(num ** 2)
        d = len(str(num))
        sq_d = len(sq)
        if num == 1:
            ans.append(num)
        elif num >= 9 and (sq_d == 2 * d or sq_d == (2 * d) - 1):
            r = int(sq[-d:])
            l = int(sq[:(sq_d - d)])
            if r + l == num:
                ans.append(num)
                
    if len(ans) == 0:
        print('INVALID RANGE')      
    else:
        print(' '.join(str(num) for num in ans))