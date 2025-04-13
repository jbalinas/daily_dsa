class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        # Pseudo--
        # 1. Initialize an empty hashmap (next_greater) to store each number's next greater element.
        # 2. Initialize an empty stack to keep track of decreasing elements.
        # 3. Traverse nums2:
        #   > While current number > top of stack:
        #     >> Pop the stack (it's the smaller number).
        #     >> Set its next greater value in the map to the current number.
        #   > Push current number onto the stack.
        # 4. After the loop, set remaining elements in stack to -1 (no greater element found).
        # 5. For each element in nums1, retrieve its next greater value from the map.

        next_greater = {}  
        stack = []         

        for num in nums2:
            while stack and num > stack[-1]:
                smaller = stack.pop()      
                next_greater[smaller] = num 

            stack.append(num)  

        for remaining in stack:
            next_greater[remaining] = -1

        return [next_greater[num] for num in nums1]
