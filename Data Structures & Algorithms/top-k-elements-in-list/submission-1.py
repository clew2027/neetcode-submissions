class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        sort_nums = sorted(freq, key=freq.get, reverse=True)

        output = []
        for i in range(k):
        
            output.append(sort_nums[i])

        return output
