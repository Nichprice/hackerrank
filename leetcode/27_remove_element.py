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

