from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Handle the edge case of an empty list
        if not nums:
            return 0
        
        # Use a set for O(1) average-case lookups
        num_set = set(nums)
        max_length = 0
        
        for num in num_set:
            # This is the key: only start counting if 'num' is the
            # beginning of a sequence (i.e., num-1 is not in the set).
            if (num - 1) not in num_set:
                current_length = 1
                
                # Now, count the length of this sequence
                while (num + current_length) in num_set:
                    current_length += 1
                
                # Update the overall max length
                max_length = max(max_length, current_length)
                
        return max_length