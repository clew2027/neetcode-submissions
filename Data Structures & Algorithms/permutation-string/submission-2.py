class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        right = 0
        seen2 = {}
        seen1 = {}
        if len(s1) > len(s2):
            return False
        while right < len(s1):
            seen2[s2[right]] = seen2.get(s2[right], 0) + 1
            seen1[s1[right]] = seen1.get(s1[right], 0) + 1
            right+=1

        while (right < len(s2)):
            if seen2 == seen1:
                return True

            seen2[s2[right]] = seen2.get(s2[right], 0) + 1
            left = right - len(s1)
            seen2[s2[left]] = seen2.get(s2[left]) - 1
            
            if seen2[s2[left]] == 0:
                seen2.pop(s2[left])
            
            right += 1
        if seen2 == seen1:
            return True
            

        return False
        