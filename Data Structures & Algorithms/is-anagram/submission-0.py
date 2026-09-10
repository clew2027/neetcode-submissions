class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        dicts = {}
        dictc = {}

        for i in range(len(s)):
            dicts[s[i]] = dicts.get(s[i], 0) + 1
            dictc[t[i]] = dictc.get(t[i], 0) + 1

        for key in dicts.keys():
            if dictc.get(key) != dicts.get(key):
                return False

        return True

            
        