class Solution:
    # # First solution: I was on the right track but sub-slicing lists is actually O(n) making the 
    # # problem have that time complexity. Instead of splitting the array, we can keep the array and just search 
    # # the subsections recursively if we keep track of the ranges to search (kind of like two pointer problems)
    # def search(self, nums: List[int], target: int) -> int:
    #     # First thought, they call out distinct integers. -> set
    #     # Solution needs to be O(log n) which means no explicit iterating (O(n)) and no merge sorting (O(n log n))
    #     # Seems like it would be beneficial to keep splitting "nums" in half 
    #     ind_div = len(nums) // 2 # "Floor" was not defined, so I looked up shorthand and it is "//"

    #     if target > nums[ind_div] and len(nums) > 1:
    #         return self.search(nums[ind_div:], target)
    #     elif target < nums[ind_div] and len(nums) > 1:
    #         return self.search(nums[:ind_div], target)
    #     else: 
    #         print(nums[ind_div])
    #         return -1 if target != nums[ind_div] else ind_div

    # Second solution (with one small fix that I haven't implemented, the base case should move 
    # before we "calc" the middle in `half_search` because that extra step is redundant)
    def search(self, nums: List[int], target: int) -> int:
        return self.half_search(0, len(nums) - 1, nums, target)
    
    def half_search(self, left: int, right: int, nums: List[int], target: int) -> int:
        middle = (left + right) // 2 

        if left > right: # Will happen if we eventually haven't found the number 
            return -1
        elif nums[middle] == target:
            return middle
        elif nums[middle] < target:
            # Left needs to be middle + 1, right can stay the same 
            return self.half_search(middle + 1, right, nums, target)
        else:
            # Right needs to be middle - 1, left can stay the same
            return self.half_search(left, middle - 1, nums, target)



        