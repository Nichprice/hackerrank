from collections import Counter

ar = [2, 10, 8, 7, 7, 7, 2, 19, 19, 8, 8, 7, 10, 2, 18, 9]
n = len(ar)

def sockMerchant1(n, ar):
    # Write your code here
    low = min(ar)
    high = max(ar)
    pairs = []
    for n in range(low, (high+1)):
        num_of_sock = 0
        for sock in ar:
            if n == sock:
                num_of_sock += 1
        if num_of_sock >= 2:
            if num_of_sock % 2 == 0:
                pairs.append(num_of_sock / 2)
            else:
                pairs.append((num_of_sock - 1) / 2)
    ans = int(sum(pairs))
    return ans

# OR
def sockMerchant2(n, ar):
    n = Counter(ar)
    print(sum(i//2 for i in n.values()))

sockMerchant2(n, ar)