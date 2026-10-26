class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        seen = {}
        left = 0
        right = 0
        maxLen = 0
        
        while (left <= right and right < len(s)):
            while (s[right] in seen and left <= right):
                seen.pop(s[left])
                left += 1
            seen[s[right]] = right
            maxLen = max(right - left + 1, maxLen)
            right += 1
                
            
        return maxLen