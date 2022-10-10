def viralAdvertising(n):
    # Write your code here
    cumulative = 0
    liked = 0
    shared = 0
    for day in range(1, (n + 1)):
        if day == 1:
            liked = 2
            cumulative = cumulative + liked
        else:
            shared = liked * 3
            liked = int(shared / 2)
            cumulative = cumulative + liked
    return cumulative