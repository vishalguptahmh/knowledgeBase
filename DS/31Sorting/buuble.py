arr = [2,5,3,1,7,6,4]

def bubble(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-1):
            if arr[j]> arr[j+1]:
                arr[j+1],arr[j] = arr[j],arr[j+1]
    return arr

def bubble_sort(my_list):
    # loop over the list n-1 times, where n is the length of the list
    # starting from the end and going backwards
    for i in range(len(my_list) - 1, 0 ,-1):
        # loop over each pair of adjacent elements up to i - 1
        for j in range(i):
            # check if the current element is greater than the next element
            if my_list[j] > my_list[j+1]:
                # if so, swap the elements using a temporary variable
                temp = my_list[j]
                my_list[j] = my_list[j+1]
                my_list[j+1] = temp
    # return the sorted list
    return my_list

print(bubble(arr))

