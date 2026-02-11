"""
list 1 : 1,2,3
list 2 : 4,5,2

find if there is any element is common or not?


first approch : 2 loops and O(n^2)
second approch : save in hashtable and check if item already there in table or not
"""

def item_in_common(l1,l2):
    dict = {}
    for i in l1:
        dict[i]=True

    for i in l2:
        if i in dict:
            return True
    return False

list1 = [1,3,5]
list2 = [2,4,5]


# print(item_in_common(list1, list2))
"""
    EXPECTED OUTPUT:
    ----------------
    True

"""