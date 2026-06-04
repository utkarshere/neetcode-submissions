class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freqnums = {}
        res = []
        for num in nums:
                freqnums[num] = freqnums.get(num, 0) + 1
        descfreqnums = dict(sorted(freqnums.items(), key=lambda x:x[1], reverse=True))
        while (k>0 and len(descfreqnums)>0):
            first = next(iter(descfreqnums))
            res.append(first)
            descfreqnums.pop(first)
            k -= 1

        return res
            

