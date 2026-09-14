class Solution:
    def search(self, nums: List[int], target: int) -> int:
        result = -1

        left = 0
        right = len(nums) - 1
        while right >= left:
            mid = int((right + left) / 2)
            if nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target: 
                left = mid + 1
            else:
                return mid
        return result

        