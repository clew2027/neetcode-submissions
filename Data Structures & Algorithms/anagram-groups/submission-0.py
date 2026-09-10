class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        dictionary = {}

        for string in strs: 
            key = [0] * 26
            for char in string:
                key[ord(char) - ord('a')] += 1

            key = tuple(key)

            if key not in dictionary:
                dictionary[key] = []

            dictionary[key].append(string);

        return list(dictionary.values())

        