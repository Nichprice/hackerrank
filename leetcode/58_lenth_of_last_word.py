class Solution:
    def lengthOfLastWord(self, s: str) -> int:

        m = len(s) - 1

        change = False

        ans = 0

        while not change and m >= 0:
            if s[m] == ' ':
                m -= 1
            
            elif s[m] != ' ':
                ans += 1
                if s[m - 1] == ' ':
                    change = True
                m -= 1
        
        return ans