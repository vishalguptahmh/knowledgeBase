

"""
----------HT: Two Sum ( ** Interview Question)------------
two_sum()

Problem:
Given an array of integers nums and a target integer target, find the indices of two numbers in the array that add up to the target.

The main challenge here is to implement this function in one pass through the array. This means you should not iterate over the array more than once. Therefore, your solution should have a time complexity of O(n), where n is the number of elements in nums.

-----

Input: nums = [5, 1, 7, 2, 9, 3], target = 10
Output: [1, 4]
Explanation: The numbers at indices 1 and 4 in the array add up to the target 10.

if not found return []
"""

def two_sum(my_list,target):
    dic = {}
    values = []
    for i,num in enumerate(my_list):
        if target - num in dic:
           return [i,dic[target-num]]
        dic[num]=i
    return values



    
    
print(two_sum([5, 1, 7, 2, 9, 3], 10))  
print(two_sum([4, 2, 11, 7, 6, 3], 9))  
print(two_sum([10, 15, 5, 2, 8, 1, 7], 12))  
print(two_sum([1, 3, 5, 7, 9], 10))  
print ( two_sum([1, 2, 3, 4, 5], 10) )
print ( two_sum([1, 2, 3, 4, 5], 7) )
print ( two_sum([1, 2, 3, 4, 5], 3) )
print ( two_sum([], 0) )



"""
    EXPECTED OUTPUT:
    ----------------
    [1, 4]
    [1, 3]
    [0, 3]
    [1, 3]
    []
    [2, 3]
    [0, 1]
    []

    def two_sum(nums,target):
    nummap = {}
    for i , num in enumerate(nums):
        complement = target - num
        if complement in nummap:
            return [nummap[complement],i]
        nummap[num]=i
    return []
"""