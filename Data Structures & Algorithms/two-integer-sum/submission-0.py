class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        for i in range(len(nums)):
            target2 = target - nums[i]
            for j in range(len(nums)):
                if j != i and nums[j] == target2:
                        return [i, j]

        