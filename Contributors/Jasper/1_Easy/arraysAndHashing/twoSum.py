class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Hashmap to store seen val/index pairs we've already seen
        seen = {}

        # Iterate through list with index/num simultaneously
        for currentIndex, currentNum in enumerate(nums):
            # Calculate complement
            complement = target - currentNum

            # If complement was seen before
            #   return indices in order
            # Else
            #   store currNum and its index
            if complement in seen:
                return[seen[complement], currentIndex]
            seen[currentNum] = currentIndex

# NOTES ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# This is a one-pass hash map solution with linear TC/SC     
# You could also do it in two passes if you really wanted to, same TC/SC
# Sorting: O(n log n) TC | linear SC
# Brute force w nested loops: O(n^2) TC | constant SC    