class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        alpha = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

        mul = columnNumber / 26
        rem = columnNumber % 26

        ans = ''
        
        
        
        if rem != 0:
            ans += alpha[rem - 1]
        
        return ans
