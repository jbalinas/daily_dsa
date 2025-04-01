# After looking at the solution, I can see that they included specific if / else blocks for each operand
# which makes sense because using "eval" is dangerous (especially in a user input context). I'm keeping this
# as my solution because it's less code but I acknowledge that it would be safer to specifically look 
# for what operand is being passed and then manually perform the op.

# I also did look up the "eval" method with the expectation that it existed.  
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ops = ['+', '-', '*', '/'] # Define all expected operators 
        res_stack = [] # Create stack for cumulative progress

        for tok in tokens: 
            if tok in ops: # If this is an operation token
                int_1 = res_stack.pop()
                int_2 = res_stack.pop() 
                eval_str = f'{int_2} {tok} {int_1}' # Order matter for how we evaluate. Specifically for division or subtraction
                result = eval(eval_str)
                res_stack.append(int(result))
            else: # This is an "int" token
                res_stack.append(int(tok))

        return 0 if not res_stack else res_stack[-1] # Return the result left in the stack. If stack is empty, return 0 (but idk if an empty set of tokens is valid RPN)