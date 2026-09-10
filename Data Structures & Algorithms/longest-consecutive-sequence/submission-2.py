class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        sorted_nums = sorted(nums)

        m = 0

        curr = sorted_nums[0]
        currLength = 1

        for i in range(1, len(sorted_nums)):
            if sorted_nums[i] - curr == 1:
                currLength += 1

            elif sorted_nums[i] - curr == 0:
                currLength += 0
            else:
                m = max(currLength, m)
                currLength = 1

            curr = sorted_nums[i]
        return max(currLength, m)


            
