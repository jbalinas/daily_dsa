class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Instantiate two dictionaries to track charcters in s and t respectively 
        s_dict = {}
        t_dict = {}

        # Early exit case - the lengths of the strings are not the same 
        if len(s) != len(t):
            return False 

        # Iterate over "s" string, keep track of the index to also get "t" character at that index
        for ind, s_char in enumerate(s):
            t_char = t[ind]
            # Commenting out code because this can be simplified 
            # if s_dict.get(s_char) is None:
            #     s_dict[s_char] = 0
            # s_dict[s_char] += 1
            
            # if t_dict.get(t_char) is None:
            #     t_dict[t_char] = 0
            # t_dict[t_char] += 1

            # Increment each dictionary
            s_dict[s_char] = s_dict.get(s_char, 0) + 1
            t_dict[t_char] = t_dict.get(t_char, 0) + 1

        # Compare dictionaries at the end 
        return s_dict == t_dict