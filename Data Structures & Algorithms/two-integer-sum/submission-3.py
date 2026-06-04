class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen = {}  # Dictionary to store number -> index

        for i, num in enumerate(nums):
            complement = target - num

            # Check if the number we need is already in our dictionary
            if complement in seen:
                # If yes, we found our pair
                return [seen[complement], i]
            
            # If not, add the current number and its index to the dictionary
            # for future lookups.
            seen[num] = i