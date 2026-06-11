class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramGroups = {} # {sorted(word): [words]}
        for word in strs:
            sortedWord = "".join(sorted(word))
            if sortedWord in anagramGroups:
                anagramGroups[sortedWord].append(word)
            else:
                anagramGroups[sortedWord] = [word]
        
        return [group for key, group in anagramGroups.items()]