class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        # Pseudo--
        # 1. Initialize an empty stack to hold operands and intermediate results.
        # 2. Traverse each token in the expression:
        #   > If token is an operator:
        #     >> Pop the two most recent operands from the stack.
        #     >> Apply the operation in the correct order: second operand op first operand.
        #     >> Push the result back onto the stack.
        #   > Else, token is a number:
        #     >> Convert to int and push onto the stack.
        # 3. The result will be the only item left in the stack after processing all tokens.

        stack = []

        for token in tokens:
            if token in {"+", "-", "*", "/"}:
                b = stack.pop()
                a = stack.pop()

                if token == "+":
                    stack.append(a + b)
                elif token == "-":
                    stack.append(a - b)
                elif token == "*":
                    stack.append(a * b)
                elif token == "/":
                    stack.append(int(a / b))  # Truncate toward zero
            else:
                stack.append(int(token))

        return stack[0]
