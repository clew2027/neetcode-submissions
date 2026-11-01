class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxCharCount = 0
        charDict = {}
        left = 0
        right = 0
        length = 0

        while right < len(s):
            charDict[s[right]] = charDict.get(s[right], 0) + 1
            maxCharCount = max(charDict[s[right]], maxCharCount)
            
            if right - left + 1 -maxCharCount > k:
                charDict[s[left]] = charDict.get(s[left])- 1
                left += 1
            length = max(length, right - left+1)
            right += 1
        return length

            
        

        