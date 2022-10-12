def permutationEquation(p):
    # Write your code here
    end = len(p)
    ans = []
    for n in range(1, (end + 1)):
        nval = p.index(n) + 1
        ans.append(p.index(nval) + 1)
    return ans