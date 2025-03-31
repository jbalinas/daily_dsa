class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
         
        # have an int array (nums)
        # if val appears >1, return true
        # else, ret false

        # initialize set for "seen" items
        seen = set()

        # iterate through the array
        for num in nums:
            # if num is already in the set, return false
            if num in seen:
                return True
            else:
                # add the num from the array to the set
                seen.add(num)

        # all nums already in the set
        # ret false
        return False

# NOTES ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# This is a hash set solution w linear (O(n)) time/space complexity.
# Other potential solutions include
# Brute force method with nested loops: O(n^2) TC and constant SC.
# Sorting: O(n log n) TC and O(1) or O(n) SC depending on sorting algo
# Use the length of the hash set: linear TC/SC, looks cleaner than hash set