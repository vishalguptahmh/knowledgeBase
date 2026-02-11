def selection_sort(my_list):
    # loop over the list n-1 times, where n is the length of the list
    for i in range(len(my_list)-1):
        # set the current index as the index of the smallest element
        min_index = i
        # loop over each element in the unsorted part of the list
        for j in range(i+1, len(my_list)):
            # if the current element is smaller than the current minimum, update the minimum index
            if my_list[j] < my_list[min_index]:
                min_index = j
        # if the index of the minimum element is not i, swap the elements at indices i and min_index
        if i != min_index:
            temp = my_list[i]
            my_list[i] = my_list[min_index]
            my_list[min_index] = temp
    # return the sorted list
    return my_list



print(selection_sort([4,2,6,5,1,3]))


 
"""
    EXPECTED OUTPUT:
    ----------------
    [1, 2, 3, 4, 5, 6]
    
 """

