from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # We could nested loop over nums twice- getting i and j until we get to the target.
        # However, this is going to be ineffecient because were going to pass over values 
        # that we've already seen (and it'll be On^2). 

        # Create dictionary to track numbers that we've seen -> their index
        num_to_ind_dict = {}

        # Iterate over nums, keep track of the index
        for ind, num in enumerate(nums):
            # Find the missing difference needed to get the target sum
            diff = target - num 
            # If we've already looked at the number, return the index pair (assuming the number
            # we've already seen is the lower index)
            if diff in num_to_ind_dict:
                return [num_to_ind_dict[diff], ind]
            # Add the number + index to the dictionary 
            num_to_ind_dict[num] = ind