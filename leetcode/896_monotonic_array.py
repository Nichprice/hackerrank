class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:

        change = 0

        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                if change == -1:
                    return False
                change = 1
            elif nums[i] < nums[i - 1]:
                if change == 1:
                    return False
                change = -1

        return True