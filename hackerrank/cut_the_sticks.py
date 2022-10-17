def cutTheSticks(arr):
    # Write your code here
    ans = []
    while len(arr) > 0:
        print(len(arr))
        ans.append(len(arr))
        low = min(arr)
        new_arr = []
        for n in range(len(arr)):
            if arr[n] > low:
                new_arr.append(arr[n] - low)
        arr = new_arr
    return ans