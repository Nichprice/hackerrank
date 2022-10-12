def nonDivisibleSubset(k, s):
  # Write your code here

  count = [0] * k

  for num in s:
    remainder = num % k
    count[remainder] += 1

  ans = min(count[0], 1) 

  if k % 2 == 0:
    ans += min(count[k//2], 1)

  for i in range(1, k//2 + 1):
    if i != k - i:
      ans += max(count[i], count[k - i])

  print(ans)