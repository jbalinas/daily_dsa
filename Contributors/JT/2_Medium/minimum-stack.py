# # First solution. This does work but the problem states that all functions must have a 
# # time complexity of O(1) - getMin is O(n). 
# class MinStack:
#     def __init__(self):
#         self.stack = [] # Initializes the stack object
#         self.frequency = defaultdict(int) # Initialize a freq dict 

#     def push(self, val: int) -> None:
#         self.stack.append(val)
#         self.frequency[val] += 1

#     def pop(self) -> None:
#         if self.stack: # Only pop if there is an entry in the stack 
#           self.frequency[self.top()] -= 1
#           self.stack.pop()

#     def top(self) -> int:
#         return self.stack[-1]
        
#     def getMin(self) -> int:
#         return min((key for key, count in self.frequency.items() if count > 0), default=None)

class MinStack:
    def __init__(self):
        self.stack = [] # Initializes the stack object
        self.min_stack = [] # Initialize a sub-stack to track the smallest object 

    def push(self, val: int) -> None:
        self.stack.append(val)
        # Add value to min stack if min stack is empty or the value is lower OR equal.
        # To be able to correctly remove values from the min stack, we have to allow duplicates   
        if not self.min_stack or val <= self.min_stack[-1]: 
            self.min_stack.append(val)

    def pop(self) -> None:
        if self.stack: # Only pop if the stack isn't empty
            lastVal = self.stack.pop() 
            if lastVal == self.min_stack[-1]:# Only remove from min-stack if the value we're popping is equal
                self.min_stack.pop()
        
    def top(self) -> int:
        return self.stack[-1]
        
    def getMin(self) -> int:
        return self.min_stack[-1]