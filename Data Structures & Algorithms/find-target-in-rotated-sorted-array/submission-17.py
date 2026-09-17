class Solution:
    def search(self, nums: List[int], target: int) -> int:
        result = -1
        left = 0
        right = len(nums) - 1

        #find cut
        while left < right:
            mid = (right + left) // 2

            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        l = 0
        r = len(nums) - 1
        
        if nums[left] <= target <= nums[-1]:
            # right side
            l = left
            r = len(nums) - 1
        else:
            # left side
            l = 0
            r = left - 1
        print(l)
        print(r)


        while l <= r:
            mid = (r + l) // 2
            print(r)
            print(l)
            if nums[mid] > target:
                r = mid - 1
            elif nums[mid] < target:
                l = mid + 1
            else:
                return mid
        return result
        




        