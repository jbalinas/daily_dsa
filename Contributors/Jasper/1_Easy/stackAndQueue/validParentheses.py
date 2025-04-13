class Solution:
    def isValid(self, s: str) -> bool:

        # Pseudo--
        # 1. Initialize an empty stack.
        # 2. Create a mapping from closing brackets to their matching opening brackets.
        # 3. For each character in the string:
        #   > If it's an opening bracket, push it to the stack.
        #   > If it's a closing bracket:
        #     >> If the stack is empty or the top of the stack doesn't match the expected opening bracket → return False.
        #     >> Otherwise, pop the top of the stack.
        # 4. After processing all characters, return True if the stack is empty (all brackets matched), else False.



        stack = []  
        pairs = {')': '(', ']': '[', '}': '{'}  

        for char in s: 
            if char in pairs.values():
                stack.append(char)  
            elif char in pairs:
                if not stack or stack[-1] != pairs[char]:
                    return False  
                stack.pop()  
                
        return not stack  
