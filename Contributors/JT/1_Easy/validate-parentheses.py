class Solution:
    # # First solution:
    # # This solution does pass all of the test cases... but will fail on inputs like this: 
    # # "[(){}]" should return True but this function returns False. 
    # def isValid(self, s: str) -> bool:
    #     # Create a dict to keep track of what beginning char should end with 
    #     openToCloseDict = {
    #         '[': ']',
    #         '{': '}',
    #         '(': ')',
    #     }
    #     # Instantiate two pointer 
    #     l, r = 0, len(s) - 1
    #     # Iterate from both sides; Return False if closing tag doesn't match the entry in the dict from above
    #     while l < r:
    #         if s[r] != openToCloseDict[s[l]]:
    #             return False
    #         l += 1
    #         r -= 1
    #     return True

	# solution using a Stack
    def isValid(self, s: str) -> bool:
        stack = []
        openToCloseDict = {
            '[': ']',
            '{': '}',
            '(': ')',
        }

        for char in s:
            if char in openToCloseDict: # This is an "open" tag
                stack.append(char)
            else: # This is a closing tag
                # If there aren't anymore opening tags to compare or the closing tag doesn't match 
                # the most recent opening tag, return False 
                if not stack or char != openToCloseDict[stack.pop()]: 
                    return False 

        # "stack" == "len(stack) != 0"
        # "not stack" == "len(stack) == 0"
        return not stack # At this point, there shouldn't be any chars in the stack unless there were unclosed opening tags 

        