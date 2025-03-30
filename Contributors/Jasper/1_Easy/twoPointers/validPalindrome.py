import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        # we are given a string and are determining if it is palindrome
        # same back and forth
        # need to make case insensitive and ignore non alpha num --> regex
        
        # We unfortunately have this committed to memory
        clean_s = re.sub(r'[^a-zA-Z0-9]', '', s.lower())

        # iterate through, push chars onto stack
        # if a char matches the one that came before it, pop off stack

        # or make it easier by reversing the string
        if clean_s == clean_s[::-1]:
            return True
        return False

# NOTES ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Reverse string solution: linear TC, constant SC




