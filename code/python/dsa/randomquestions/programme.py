# Given an array arr[] denoting heights of n towers and a positive integer k.

# For each tower, you must perform exactly one of the following operations exactly once.

# Increase the height of the tower by k
# Decrease the height of the tower by k
# Find out the minimum possible difference between the height of the shortest and tallest towers after you have modified each tower.

# You can find a slight modification of the problem here.
# Note: It is compulsory to increase or decrease the height by k for each tower. After the operation, the resultant array should not contain any negative integers.

# Examples :

# Input: k = 2, arr[] = [1, 5, 8, 10]
# Output: 5
# Explanation: The array can be modified as [1+k, 5-k, 8-k, 10-k] = [3, 3, 6, 8]. The difference between the largest and the smallest is 8-3 = 5.
# Input: k = 3, arr[] = [3, 9, 12, 16, 20]
# Output: 11
# Explanation: The array can be modified as [3+k, 9+k, 12-k, 16-k, 20-k] = [6, 12, 9, 13, 17]. The difference between the largest and the smallest is 17-6 = 11. 

arr = [1,5,8,10]
k = 2
output = 5

arr2 = [3,9,12,16,20]
k2 = 3
output2=  11

arr3 = [1,8,10,6,4,6,9,1]
k3 = 7
output3=  9


def getMinDiff(arr,k):
    arr.sort()
    n = len(arr)

    ans = arr[n-1]-arr[0]

    for i in range(n-1):
        print(i)
        min_h = 999
        if arr[0]+k < arr[i+1]-k:
            min_h = arr[0]+k
        else:
            min_h = arr[i+1]-k
        
        if min_h<0:
            continue
        max_h = 0
        if arr[i]+k<arr[n-1]-k:
            max_h = arr[n-1]-k
        else:
            max_h = arr[i]+k

        if ans> max_h-min_h:
            ans = max_h-min_h
            print("anser",ans)


getMinDiff(arr3,k3)