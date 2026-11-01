class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}


        # def dp(index):
        #     if index >= len(nums):
        #         return 0
        #     print(index)
        #     return max(dp(index + 1), dp(index + 2) + nums[index])

        # return dp(0)

        def dp(index):
            if index >= len(nums):
                return 0
            if index in memo:
                return memo[index]
            skip = dp(index + 1)
            noSkip = dp(index + 2) + nums[index]
            memo[index] = max(skip, noSkip)
            return memo[index]

        return dp(0)
        