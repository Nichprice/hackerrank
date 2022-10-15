def findDigits(n):
  # Write your code here
    counter = 0
    nums = list(str(n))
    for num in nums:
        num = int(num)
        if num == 0:
            counter = counter
        elif n % num == 0:
            counter += 1
    return counter