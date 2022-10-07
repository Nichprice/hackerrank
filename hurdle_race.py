def hurdleRace(k, height):
    # Write your code here
    tallest = max(height)
    ans = tallest - k
    if k < tallest:
        return ans
    else:
        return 0