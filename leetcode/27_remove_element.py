## this solution is how you would do it in an interview
## set a left pointer and a right pointer
## move the left pointer every time you encounter a unique number
## always move the right pointer
## return the left pointer (number of unique numbers)


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        l = 1
        r = 1
        val = nums[0]

        while r < len(nums):
            if nums[r] != nums[l - 1]:
                nums[l] = nums[r]
                l += 1
                r += 1
            else:
                r += 1

        return l


## this solution is very bad

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        threes = 0

        for num in nums:
            if num == val:
                threes += 1
        
        removed = 0
        i = 0

        while removed < threes:
            if nums[i] == val:
                nums.pop(i)
                removed += 1
            else:
                i += 1

        return len(nums)



