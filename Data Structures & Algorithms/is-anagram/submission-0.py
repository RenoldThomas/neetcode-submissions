class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sDict = {}
        for letter in s:
            if letter in sDict:
                sDict[letter] += 1
            else: 
                sDict[letter] = 1
        
        tDict = {}
        for letter in t:
            if letter in tDict:
                tDict[letter] += 1
            else: 
                tDict[letter] = 1

        return sDict == tDict