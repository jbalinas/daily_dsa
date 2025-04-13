class MinStack:
    def __init__(self):
        """
        Initialize data structure.
        - `self.stack` stores all values pushed onto the stack.
        - `self.min_stack` keeps track of the current minimums.
        """
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        """
        Pushes an integer `val` onto the stack.
        Also updates the min stack if `val` is the new minimum.
        Time: O(1)
        """
        self.stack.append(val)
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self) -> None:
        """
        Removes the element on the top of the stack.
        If the top element is the current minimum, it is also removed from the min stack.
        Time: O(1)
        """
        if self.stack:
            val = self.stack.pop()
            if val == self.min_stack[-1]:
                self.min_stack.pop()

    def top(self) -> int:
        """
        Returns the element on the top of the stack without removing it.
        Time: O(1)
        """
        return self.stack[-1]

    def getMin(self) -> int:
        """
        Retrieves the minimum element in the stack.
        Time: O(1)
        """
        return self.min_stack[-1]
