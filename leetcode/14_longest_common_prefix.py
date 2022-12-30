class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        lengs = []
        for word in strs:
            lengs.append(len(word))

        short = min(lengs)
        
        ans = ""

        for i in range(short):
            same = True
            for j in range(len(strs)):
                if strs[j][i] != strs[0][i]:
                    same = False

            if same:
                ans += strs[0][i]
            else:
                break
        
        return ans