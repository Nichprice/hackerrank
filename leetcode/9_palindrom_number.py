class Solution:
    def isPalindrome(self, x: int) -> bool:

        x = str(x)
        ans = True

        i = 0
        j = len(x) - 1

        while i < j:
            if x[i] != x[j]:
                ans = False
                return ans
            i += 1
            j -= 1

        return ans