# Set: Longest Consecutive Sequence ( ** Interview Question)
# Given an unsorted array of integers, write a function that finds the length of the  longest_consecutive_sequence (i.e., sequence of integers in which each element is one greater than the previous element).

# Use sets to optimize the runtime of your solution.

# Input: An unsorted array of integers, nums.

# Output: An integer representing the length of the longest consecutive sequence in nums.

# Example:



# Input: nums = [100, 4, 200, 1, 3, 2]
# Output: 4
# Explanation: The longest consecutive sequence in the input array is [4, 3, 2, 1], and its length is 4.


def longest_consecutive_sequence(nums):
    # Create a set to keep track of the numbers in the array
    num_set = set(nums)
    longest_sequence = 0
    
    # Loop through the numbers in the nums array
    for num in nums:
        # Check if the current number is the start of a new sequence
        if num - 1 not in num_set:
            current_num = num
            current_sequence = 1
            
            # Keep incrementing the current number until the end of the sequence is reached
            while current_num + 1 in num_set:
                current_num += 1
                current_sequence += 1
            
            # Update the longest sequence if the current sequence is longer
            longest_sequence = max(longest_sequence, current_sequence)
    
    return longest_sequence

print( longest_consecutive_sequence([100, 4, 200, 1, 3, 2]) )



"""
    EXPECTED OUTPUT:
    ----------------
    4

"""