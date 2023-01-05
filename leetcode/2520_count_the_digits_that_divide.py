class Solution:
    def countDigits(self, num: int) -> int:

        ans = 0

        string = str(num)

        for i in range(len(string)):
            val = int(string[i])
            if num % val == 0:
                ans += 1

        return ans
        