class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        memo = {}

        def dp(index, end):
            if index >= end:
                return 0
            if (index, end) in memo.keys():
                return memo[(index, end)]
            memo[(index, end)] = max(dp(index + 1, end), dp(index + 2, end) + nums[index])
            return memo[(index, end)]
        return max(dp(0, len(nums) - 1), dp(1, len(nums)))