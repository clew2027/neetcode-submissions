class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        right = 0
        left = 0
        maxLen = 0
        seen= {}
        while right >= left and right < len(s):
            seen[s[right]] = seen.get(s[right], 0) + 1
            max_freq = max(seen.values())
            while(right - left + 1 - max_freq > k):
                seen[s[left]] -= 1
                if seen[s[left]] == 0:
                    seen.pop(s[left])
                max_freq = max(seen.values())
                left+=1
            maxLen = max(right-left + 1, maxLen)
            right += 1

        return maxLen

        