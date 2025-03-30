class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # UNDERSTAND
        # This is a frequency dictionary problem.

        # PLAN --> IMPLEMENT

        # Early exit if lengths are different
        if len(s) != len(t):
            return False

        # Create frequency dictionaries for both strings
        s_freq_dict = {}
        t_freq_dict = {}

        for char in s:
            if char not in s_freq_dict:
                s_freq_dict[char] = 0
            s_freq_dict[char] += 1

        for char in t:
            if char not in t_freq_dict:
                t_freq_dict[char] = 0
            t_freq_dict[char] += 1

        # Compare the two frequency dictionaries
        return s_freq_dict == t_freq_dict

# NOTES ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# O(n) TC, O(1) SC here due to limited charset but O(n) worst case

# CLEANER SOLUTION -- same TC/SC
# Uses one freqdict; updates pos with s and neg w t         
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        freq = {}
        for i in range(len(s)):
            freq[s[i]] = freq.get(s[i], 0) + 1
            freq[t[i]] = freq.get(t[i], 0) - 1

        return all(count == 0 for count in freq.values())
