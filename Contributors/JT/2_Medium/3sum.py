class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # We could sort nums which could be ineffecient O(n log n)
        # Brute force is definitely a triple nested array but O(n^3) and migth be an issue with duplicates 

        # result (list of lists)
        res = []
        # sort 
        nums.sort()
        
        # -1, 0, 1, 2, -1, -4
        # becomes 
        # -4, -1, -1, 0, 1, 2

        for i, a in enumerate(nums): # Loop through each number and isolate so that we can create a classic two-pointer problem
            if i > 0 and a == nums[i - 1]: # Skip this iteration if "a" is a duplicate  
                continue
            left, right = i + 1, len(nums) - 1 # Set our two pointers 
            while left < right:
                threeSum = a + nums[left] + nums[right] # Create a sum of three numbers
                if threeSum > 0: # We already sorted- so if the sum is too big, we should decrement the right pointer
                    right -= 1
                elif threeSum < 0: # Likewise, if the sum is too small, we should incremenet the left pointer 
                    left += 1
                else:
                    # Assuming that we've found a triplet - Add it to the result
                    res.append([a, nums[left], nums[right]])
                    # Need to update pointers so we don't get stuck at this point
                    # I had to look this up :S
                    left += 1 # To avoid duplidates, we should iterate the left pointer 
                    while nums[left] == nums[left -1] and left < right: # But they could be duplicates. So we make sure they're not the same. 
                        left += 1
        return res
        