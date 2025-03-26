class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Sanitize the word to remove non alphanumerical characters + make lower case 
        sanitized = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
        # Get a reference of the left and right sides of the sanitized sentence 
        left = 0
        right = len(sanitized) - 1

        # Iterate while shrinking the bounds from both directions. Return false if 
        # the chars don't match 
        while left < right:
            if sanitized[left] != sanitized[right]:
                return False
            left += 1
            right -= 1

        return True
        