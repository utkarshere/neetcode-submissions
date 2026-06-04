class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        dup = {}
        for num in nums:
            if num in dup:
                return True
            else:
             dup[num] = dup.get(num, 0) + 1
        return False
    