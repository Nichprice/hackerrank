class Solution:
    def longestPalindrome(self, s: str) -> int:
        s =  Counter(s)
        tots = 0
        yet = False
        for i in s:
            if s[i] % 2 != 0:
                if yet == False:
                    tots += s[i]
                    yet = True
                else:
                    tots += (s[i] - 1)
            else:
                tots += s[i]
    
        return tots