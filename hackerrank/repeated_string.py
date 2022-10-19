def repeatedString(s, n):
    # Write your code here
    s = list(s)
    counter = 0
    for let in s:
        if let == 'a':
            counter += 1
    repeats = int(n/len(s))
    left_overs = n % len(s)
    extras = 0
    for n in range(left_overs):
        if s[n] == 'a':
            extras += 1
    ans = counter * repeats + extras
    return ans