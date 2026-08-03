class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
        
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    # WRITE MERGE METHOD HERE #
    #                         #
    #                         #
    #                         #
    #                         #
    ###########################
    
    def merge(self,linklist2):
        list1 = self.head
        list2 = linklist2.head
        combined = Node(0)
        mergedlist = combined
        
        while list1 is not None and list2 is not None:
            if list1.value< list2.value:
                combined.next = list1
                list1 = list1.next
                
            else:
                combined.next = list2
                list2 = list2.next
            combined = combined.next
        
        if list1 is not None:
            combined.next = list1

        if list2 is not None:
            combined.next = list2

        if mergedlist is not None : 
            mergedlist = mergedlist.next
        
        self.head = mergedlist
        temp  = mergedlist
        while temp.next is not None: 
            temp = temp.next
        self.tail = temp
    


l1 = LinkedList(1)
l1.append(3)
l1.append(5)
l1.append(7)


l2 = LinkedList(2)
l2.append(4)
l2.append(6)
l2.append(8)

l1.merge(l2)

l1.print_list()


"""
    EXPECTED OUTPUT:
    ----------------
    1 
    2 
    3 
    4 
    5 
    6 
    7
    8

"""