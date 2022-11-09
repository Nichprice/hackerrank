def strangeCounter(t):
    # Write your code here
    counter = 0
    time = 1
    times0 = [1]
    while time <= t:
        time += (2**counter * 3)
        times0.append(time)
        counter += 1
    counter = counter - 1
    value0 = 2**counter * 3
    ans = value0 - (t - times0[-2])
    return ans