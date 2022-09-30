def migratoryBirds(arr):
    # Write your code here
    bird_count = [0, 0, 0, 0, 0]
    for bird in arr:
        bird_count[bird - 1] += 1
    max = 0
    bird_type = 0
    for n in range(0, 5):
        print(n)
        if bird_count[n] > max:
            max = bird_count[n]
            bird_type = (n + 1)
    return bird_type