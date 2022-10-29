def beautifulTriplets(d, arr):
    r = max(arr) + 1
    counter = [0] * r
    triplets = 0
    for num in arr:
        counter[num] += 1
    for i in range(n - 2):
        if arr[i] <= (max(arr) - 2 * d):
            if counter[arr[i] + d] != 0 and counter[arr[i] + 2 * d] != 0:
                triplets += 1
        
    return triplets
      