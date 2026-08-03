"""
Write a function named stream_max that takes as its input a list of integers (nums). The function should return a list of the same length, where each element in the output list is the maximum number seen so far in the input list.

More specifically, for each index i in the input list, the element at the same index in the output list should be the maximum value among the elements at indices 0 through i in the input list.

Use the provided MaxHeap class to solve this problem. You should not need to modify the MaxHeap class to complete this task.

Function Signature: def stream_max(nums):

Examples:
If the input list is [1, 3, 2, 5, 4], the function should return [1, 3, 3, 5, 5].
Explanation:
At index 0, the maximum number seen so far is 1.
At index 1, the maximum number seen so far is 3.
At index 2, the maximum number seen so far is still 3.
At index 3, the maximum number seen so far is 5.
At index 4, the maximum number seen so far is still 5.
So, the output list is [1, 3, 3, 5, 5].

Similarly, if the input list is [7, 2, 4, 6, 1], the function should return [7, 7, 7, 7, 7].
Explanation:
At each index, the maximum number seen so far is 7.
So, the output list is [7, 7, 7, 7, 7].

Constraints:
You may assume that the input list does not contain any null or undefined elements.

"""

from MaxHeap import MaxHeap

def stream_max(nums):
    if len(nums) == 0:
        return []
    max_value  =  nums[0]
    
    for i,num in enumerate(nums):
        if num < max_value:
          nums[i] = max_value
        else:
            max_value = num
    return nums


def stream_max(nums):
    max_heap = MaxHeap()
    max_stream = []
 
    for num in nums:
        max_heap.insert(num)
        max_stream.append(max_heap.heap[0])
 
    return max_stream


test_cases = [
    ([], []),
    ([1], [1]),
    ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
    ([1, 2, 2, 1, 3, 3, 3, 2, 2], [1, 2, 2, 2, 3, 3, 3, 3, 3]),
    ([-1, -2, -3, -4, -5], [-1, -1, -1, -1, -1])
]

for i, (nums, expected) in enumerate(test_cases):
    result = stream_max(nums)
    print(f'\nTest {i+1}')
    print(f'Input: {nums}')
    print(f'Expected Output: {expected}')
    print(f'Actual Output: {result}')
    if result == expected:
        print('Status: Passed')
    else:
        print('Status: Failed')



"""
    EXPECTED OUTPUT:
    ----------------
    Test 1
    Input: []
    Expected Output: []
    Actual Output: []
    Status: Passed
    Test 2
    Input: [1]
    Expected Output: [1]
    Actual Output: [1]
    Status: Passed
    Test 3
    Input: [1, 2, 3, 4, 5]
    Expected Output: [1, 2, 3, 4, 5]
    Actual Output: [1, 2, 3, 4, 5]
    Status: Passed
    Test 4
    Input: [1, 2, 2, 1, 3, 3, 3, 2, 2]
    Expected Output: [1, 2, 2, 2, 3, 3, 3, 3, 3]
    Actual Output: [1, 2, 2, 2, 3, 3, 3, 3, 3]
    Status: Passed
    Test 5
    Input: [-1, -2, -3, -4, -5]
    Expected Output: [-1, -1, -1, -1, -1]
    Actual Output: [-1, -1, -1, -1, -1]
    Status: Passed

"""
