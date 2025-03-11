from typing import List

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # Set to track ints that we've already seen
        seen = set()

        # Iterate over ints
        for num in nums:
            # Return True if the int is already in the set
            if num in seen:
                return True
            # Add the int to the set
            seen.add(num)

        # We can assume there are no duplicates by this point
        return False