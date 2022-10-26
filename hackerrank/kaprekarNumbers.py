def kaprekarNumbers(p, q):
    # Write your code here
    ans = []
    for num in range(p, q + 1):
        sq = num ** 2
        string = str(sq)
        d = len(str(num))
        sq_d = len(string)
        if num == 1:
            ans.append(num)
        elif num >= 9 and (sq_d == 2 * d or sq_d == (2 * d) - 1):
            r = int(string[-d:])
            l = int(string[:(sq_d - d)])
            if r + l == num:
                ans.append(num)
                
    if len(ans) == 0:
        print('INVALID RANGE')      
    else:
        print(' '.join(str(num) for num in ans))