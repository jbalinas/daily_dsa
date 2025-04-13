class Solution:
    def dailyTemperatures(self, temps: List[int]) -> List[int]:
        
        # Pseudo--
        # 1. Initialize a result list with 0s, same length as temps.
        # 2. Initialize an empty stack to store indices of unresolved temperatures.
        # 3. Traverse the temps list:
        #   > While stack is not empty and current temp > temp at index on top of stack:
        #     >> Pop the index from the stack.
        #     >> Set result at that index to the difference between current index and popped index.
        #   > Push current index to the stack.
        # 4. Return the result list after processing all temps.

        res = [0] * len(temps)
        stack = []

        for day_index, temp in enumerate(temps):
            while stack and temp > temps[stack[-1]]:
                prev_index = stack.pop()
                res[prev_index] = day_index - prev_index
            stack.append(day_index)

        return res
