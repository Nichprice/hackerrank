

## O(n^2)


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        for i in range(len(nums) - 1):
            for j in range((i+1), len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]


# can you make something quicker than O(n^2)

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lagmap = {} ## val : index

        for i, n in enumerate(nums):
            diff = target - n
            if diff in lagmap:
                return [lagmap[diff], i]

            lagmap[n] = i

        return