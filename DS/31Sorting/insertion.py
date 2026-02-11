

def insertion_sort(my_list):
    # iterate over each element of the list starting from the second element
    for i in range(1, len(my_list)):
        # store the current element being sorted in a temporary variable
        temp = my_list[i]
        # iterate over the already sorted part of the list
        j = i-1
        # while the current element is less than the previous element and the index is still in bounds
        while temp < my_list[j] and j > -1:
            # swap the current element with the previous element
            my_list[j+1] = my_list[j] 
            my_list[j] = temp
            # decrement the index j
            j -= 1
    # return the sorted list
    return my_list      


print(insertion_sort([4,2,6,5,1,3]))



"""
    EXPECTED OUTPUT:
    ----------------
    [1, 2, 3, 4, 5, 6]
    
 """

