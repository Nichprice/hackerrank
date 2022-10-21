def equalizeArray(arr):
  # Write your code here
  counter = [0] * (max(arr) + 1)
  for num in arr:
    counter[num] += 1
  return len(arr) - max(counter)