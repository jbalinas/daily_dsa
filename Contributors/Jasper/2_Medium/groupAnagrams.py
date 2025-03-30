class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # Dict to group words by their sorted character key
        anagram_map = defaultdict(list)  

        for word in strs:
            # Sort the characters in the word to form the grouping key
            key = ''.join(sorted(word))
            # Add the original word to the list of its corresponding anagram group  
            anagram_map[key].append(word)  

        # Return the grouped anagram lists
        return list(anagram_map.values())  

# NOTES ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# O(m * n log n) TC | O(m*n) SC