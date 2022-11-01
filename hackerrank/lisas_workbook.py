def workbook(n, k, arr):
  # Write your code here
  ans = 0
  page = 1

  for probs in arr:
    for problem in range(1, probs + 1):
      if problem == page:
        ans += 1

      if problem == probs or problem % k == 0:
        page += 1
  print(ans)