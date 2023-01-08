class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        digits.reverse()

        for i in range(len(digits)):
            if digits[i] != 9:
                digits[i] = digits[i] + 1
                break
            else: 
                digits[i] = 0
                if i == len(digits) - 1:
                    digits.append(1)
            

        digits.reverse()

        return digits
        