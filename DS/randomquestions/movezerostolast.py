
def pushZerosToEnd(arr):
    i = 0
    j = 1
    l = len(arr)

    while i < l and j< l : 
        if j< i : 
            j = i
        if arr[i] == 0 and arr[j] !=0:
            arr[i],arr[j] = arr[j],arr[i]
        elif arr[i]!=0:
            i+=1
        else:
            j+=1
    return arr

# arr = [1, 2, 0, 4, 3, 0, 5, 0]
# expect = [1, 2, 4, 3, 5, 0, 0, 0]


arr = [0 ,0 ,0 ,3 ,1, 4]
expect = [3, 1, 4, 0, 0, 0]
# output = pushZerosToEnd(arr)

# print(output)

# print(output == expect)


def rotateArr(arr, d):
    d = d% len(arr)
    print( d)
    if d == 0 :
        return arr
    temp = []
    k = 0 
    for i in range(len(arr)):
        if k < d:
            temp.append(arr[i])
            k+=1
        else:
            arr[i-d] = arr[i]
    
    l = len(arr)
    for i in range(d):
        arr[l-d+i] = temp[i]

    return arr


def rRotate(arr,d):
    l = len(arr)
    d = d %l
    reverse(arr,0,l-1)
    reverse(arr,l-d,l-1)
    reverse(arr,0,l-d-1)

    return arr

def reverse(arr,i,j):
    while i < j:
        arr[i],arr[j] = arr[j],arr[i]
        i+=1
        j-=1

# arr = [1,2,3,4,5]
# expoutput = [3,4,5,1,2]
arr = [ 2, 4, 6, 8, 10, 12 ,14, 16 ,18 ,20]
exp = [8, 10, 12 ,14 ,16, 18, 20, 2, 4, 6]

k = 3

output = rRotate(arr,k)

# print(exp ==output)
# print(output)
    	

s = "abcd"
def permutation(s):
    arr=[]
    def backtrack(path,remaining):
        if not remaining:
            arr.append(path)
            return
    
        for i in range(len(remaining)):
            backtrack(path+remaining[i],remaining[:i]+remaining[i+1:])
        
    backtrack("",s)
    return arr

# print(permutation(s))


def next_permutation(arr):
    n = len(arr)

    # Step 1: find pivot
    i = n - 2
    while i >= 0 and arr[i] >= arr[i + 1]:
        i -= 1

    if i == -1:
        return False  # last permutation

    # Step 2: find successor
    j = n - 1
    while arr[j] <= arr[i]:
        j -= 1

    # Step 3: swap
    arr[i], arr[j] = arr[j], arr[i]

    # Step 4: reverse suffix
    arr[i + 1:] = reversed(arr[i + 1:])

    return True

def next_permutations(arr):
    l = len(arr)
    i = l-2
    while i >=0 and arr[i]>arr[i+1]:
        i = i-1
    
    if i <0:
        return False
    
    j = l-1

    while arr[j]<arr[i]:
        j=j-1

    # swap
    arr[j],arr[i]=arr[i],arr[j]

    reverse(arr,i+1,l-1)

    return True
def all_permutations(s):
    arr = sorted(s)
    result = [''.join(arr)]

    while next_permutations(arr):
        result.append(''.join(arr))

    return result

def all_permutation(s):
    arr = sorted(s)
    result = [''.join(arr)]

    while next_permutation(arr):
        result.append(''.join(arr))

    return result

# print("pring ")
# print(all_permutations("abcd"))
# print(all_permutation("abcd"))



# Given an array of integers arr[] representing a permutation, implement the next permutation that rearranges the numbers into the lexicographically next greater permutation. If no such permutation exists, rearrange the numbers into the lowest possible order (i.e., sorted in ascending order). 

# Note:  A permutation of an array of integers refers to a specific arrangement of its elements in a sequence or linear order.

# Examples:

# Input: arr[] = [2, 4, 1, 7, 5, 0]
# Output: [2, 4, 5, 0, 1, 7]
# Explanation: The next permutation of the given array is [2, 4, 5, 0, 1, 7].
# Input: arr[] = [3, 2, 1]
# Output: [1, 2, 3]
# Explanation: As arr[] is the last permutation, the next permutation is the lowest one.
# Input: arr[] = [3, 4, 2, 5, 1]
# Output: [3, 4, 5, 1, 2]
# Explanation: The next permutation of the given array is [3, 4, 5, 1, 2].

dic={}
dic[2, 4, 1, 7, 5, 0] = [2, 4, 5, 0, 1, 7]
dic[3, 2, 1]=[1, 2, 3]
dic[3, 4, 2, 5, 1] = [3, 4, 5, 1, 2]


def checkResult():

    for i in dic:
        output = findNext(list(i))
        if dic[i] == output:
            print(f"passed {i} and output {output}")
        else:
            print("Failed")



def findNext(arr):
    l = len(arr)

    i = l -2

    while i >=0 and arr[i]>=arr[i+1]:
        i-=1
    
    if i < 0:
        return sorted(arr)
    j = l-1

    while arr[j]<=arr[i]:
        j-=1

    # swap
    arr[i],arr[j]=arr[j],arr[i]

    # arr[i+1:]=reversed(arr[i+1:])
    arr[i + 1:] = arr[i + 1:][::-1]

    return arr
    
    
# checkResult()
# print(findNext([2, 4, 1, 7, 5, 0]))


def maximumProfit( prices) -> int:
        # check next number if its greater than only buy
        maxprofit = 0
        minprice = prices[0]
        for i in range(1,len(prices)):
            if prices[i]<prices[i-1]:
                minprice = prices[i]
            else:
                maxprofit = max(maxprofit,prices[i]-minprice)
        return maxprofit

# prices = [100, 180, 260, 310, 40, 535, 695]
prices = [4, 2, 2, 2, 4]
print(maximumProfit(prices))


def getMinDiff( arr, k):
        mi = arr[0]
        ma = arr[0]
       
        for i in arr:
            if i < mi:
                mi = i
            elif i > ma:
                ma = i 
            
        diff = ma - mi - 2*(k)

        return diff   
print(getMinDiff([1, 8, 10, 6, 4, 6, 9, 1],7))