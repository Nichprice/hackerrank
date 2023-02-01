class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        nums = sorted(nums)
        l = 0
        r = 1

        while r <= len(nums) - 1:
            if nums[l] == nums[r]:
                return True
            else:
                l += 1
                r += 1
            
        return False