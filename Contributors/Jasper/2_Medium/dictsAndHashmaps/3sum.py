class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
       
        # Sort the input list to make it easier to handle duplicates and use two-pointer logic
        nums.sort() 
        # Count occurrences of each number 
        number_frequency = defaultdict(int) 

        for number in nums:
            number_frequency[number] += 1

        # Store all valid triplets that sum to 0
        result = []  

        for first_index in range(len(nums)):
            first_number = nums[first_index]
            number_frequency[first_number] -= 1 

            # Skip duplicate first numbers
            if first_index > 0 and first_number == nums[first_index - 1]:
                continue

            for second_index in range(first_index + 1, len(nums)):
                second_number = nums[second_index]
                number_frequency[second_number] -= 1  

                # Skip duplicate second numbers
                if second_index > first_index + 1 and second_number == nums[second_index - 1]:
                    continue

                # Calculate the third number needed to sum to 0
                third_number = -(first_number + second_number)

                # Check if the third number exists in remaining numbers
                if number_frequency[third_number] > 0:
                    result.append([first_number, second_number, third_number])

            # Restore second numbers' frequencies for the next iteration of first_number
            for second_index in range(first_index + 1, len(nums)):
                second_number = nums[second_index]
                number_frequency[second_number] += 1

        return result

# NOTES ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Hashmap solution: O(n^2) TC | O(n) SC
# You could do 2ptr but you'd still get the same TC/SC
# Brute force would be disgarsting    