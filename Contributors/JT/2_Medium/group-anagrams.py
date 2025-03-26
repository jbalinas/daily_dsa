class Solution:
    # Original solution. 
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Create a dictionary. The key will be a sorted string (E.g., "cats" becomes "acst"), 
        # the value will be an array of anagrams 
        dictionary = {}
        for word in strs: # Iterating every word is O(n)  
            key = ''.join(sorted(word)) # Sorting a word is O( k log k)
            if key not in dictionary:
                dictionary[key] = []
            dictionary[key].append(word)

        return dictionary.values() # Solution would be O(n * k log k)

    # # Solution after looking at hints / researching Python functions:  
    # # Things that I had to look up:
    #     # Creating a frequency counter - ([0] * n) created a dictionary of length n with '0's for all indexes
    #     # tuple - hashable list (if elements are all hashable). Also immutable.   
    #     # defaultdict - part of 'collections', allows us to bypass "initialization" checks :) 
    #     # ord(char) returns the Unicode code point of the given character
    # def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    #     dictionary = defaultdict(list)
    #     for word in strs:
    #         char_arr = [0] * 26 # Create array of possible elements 
    #         for char in word:
    #             char_arr[ord(char) - ord('a')] += 1 # Modify the frequency counter
    #         dictionary[tuple(char_arr)].append(word) # Add key + word to dictionary
    #     return list(dictionary.values())


             