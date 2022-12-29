class Solution:
    def romanToInt(self, s: str) -> int:
        
        e = len(s) - 1
        tot = 0
        
        for i in range(len(s)):
            if i < e:
                if s[i] == "I":
                    if s[i + 1] == "V" or s[i + 1] == "X":
                        tot -= 1
                    else:
                        tot += 1
                
                if s[i] == "V":
                    tot += 5
                
                if s[i] == "X":
                    if s[i + 1] == "L" or s[i + 1] == "C":
                        tot -= 10
                    else:
                        tot += 10
                
                if s[i] == "L":
                    tot += 50

                if s[i] == "C":
                    if s[i + 1] == "D" or s[i + 1] == "M":
                        tot -= 100
                    else:
                        tot += 100
                
                if s[i] == "D":
                    tot += 500

                if s[i] == "M":
                    tot += 1000
            
            else:
                if s[i] == "I":
                    tot += 1
                if s[i] == "V":
                    tot += 5
                if s[i] == "X":
                    tot += 10
                if s[i] == "L":
                    tot += 50
                if s[i] == "C":
                    tot += 100
                if s[i] == "D":
                    tot += 500
                if s[i] == "M":
                    tot += 1000
        
        return tot