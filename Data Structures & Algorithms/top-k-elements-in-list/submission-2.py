class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numCounts = {} # {num: count}
        for num in nums:
            if num in numCounts:
                numCounts[num] += 1
            else:
                numCounts[num] = 1
        
        sortedNums = sorted(numCounts.keys(), key=lambda num:numCounts[num], reverse=True)
        return sortedNums[:k]