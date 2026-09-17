class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        seen = {}
        left = 0
        right = 0
        maxLen = 0
        while right < len(s):
            if s[right] in seen:
                left = max(seen[s[right]] + 1, left)
            seen[s[right]] = right
            right += 1
            maxLen = max(right - left, maxLen)

        return maxLen

        