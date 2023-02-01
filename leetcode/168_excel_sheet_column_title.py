class Solution:
    def convertToTitle(self, n: int) -> str:
        
        ans = ''

        while n > 0:
            c = chr(ord('A') + (n - 1) % 26)
            ans = c + ans
            n = (n - 1) // 26

        return ans
        