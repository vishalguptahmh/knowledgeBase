class Node :
    def __init__ (self,value):
        self.value = value
        self.next = None
        
class LinkedList :
    def __init__ (self,value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def append(self,value):
        print(f"{value} Adding to tail")
        new_node = Node(value)
        if self.head is None : 
            self.head = new_node
            self.tail = new_node
        else : 
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return new_node
    
    def prepend(self,value):
        print("adding to head")
        if self.head is None:
            self.head = Node(value)
        else:
            temp = self.head
            new_node = Node(value)
            new_node.next = self.head
            self.head = new_node

    def print_list(self):
        self.printList()

    def printList(self):
        print("-----------------------------------")
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

        print('Head:', self.head.value)
        print('Tail:', self.tail.value)
        print('Length:', self.length)
        print("-----------------------------------")

    def remove(self):
    
        if self.head is None : 
            print("Removing from head- List is empty")
            return None
        self.length -= 1
        print("Removing from head Value : ",self.head.value)
        self.head = self.head.next

    def removeFromEnd(self):
        print("Removing from tail")
        if self.head is None: return None
        else: 
            temp = self.head
            while temp.next != self.tail:
                temp = temp.next
            self.tail = temp
            self.tail.next = None
            self.length -= 1    

    def has_loop(self):
        if self.head is None: return False
        
        slow = self.head
        fast = self.head

        while fast is not None and fast.next is not None and fast != slow:
            slow = slow.next
            fast = fast.next.next
    
        if fast == slow:
            return True
        else : 
            return False

    def remove_duplicates(self):
        current = self.head
        runner = self.head

        while current :
            runner = current
            while runner is not None and runner.next is not None:
                if runner.next.value == current.value:
                    runner.next = runner.next.next
                    self.length -= 1
                runner = runner.next
            current = current.next

    def remove_duplicates_with_set(self):
        # Remove duplicates using a set
        current = self.head
        seen = set()
        seen.add(current.value)
        while current is not None and current.next is not None:
            if current.next.value in seen:
                current.next = current.next.next
                self.length -= 1
            else:
                seen.add(current.next.value)
            current = current.next

    def binary_to_decimal(self):
        current = self.head
        decimal = 0
        while current is not None:
            decimal = decimal*2+current.value
            current = current.next
        return decimal        

def find_kth_from_end(ll,k):
    slow=fast=ll.head
    for _ in range(k):
        if fast is None:
            return None
        fast = fast.next

    while fast is not None:
        slow= slow.next
        fast = fast.next

    return slow

    



# my_linked_list = LinkedList(1)


# my_linked_list.append(2)
# my_linked_list.append(3)
# my_linked_list.append(4)
# my_linked_list.printList()

# Find Loop in linklist 
# my_linked_list.tail.next = my_linked_list.head
# print('hasLoop:', my_linked_list.has_loop())

# Kth Node from END
# k = 2
# result = find_kth_from_end(my_linked_list, k)
# print("Kth Node is", result.value if result is not None else "None")  # Output: 4

# Remove Duplicates
# 1. using nested loop = O(n2)
# 2. using set = O(n)
# my_linked_list.append(3)
# my_linked_list.append(1)
# my_linked_list.remove_duplicates()
# my_linked_list.printList()
# my_linked_list.append(3)
# my_linked_list.append(1)
# my_linked_list.remove_duplicates_with_set()
# my_linked_list.printList()

my_linked_list = None



# Test case 1: Binary number 110 = Decimal number 6
linked_list = LinkedList(1)
linked_list.append(1)
linked_list.append(0)
print("Test case 1 linked list:")
linked_list.printList()
result = linked_list.binary_to_decimal()
try:
    assert result == 6
    print("Test case 1 passed, returned:", result)
except AssertionError:
    print("Test case 1 failed, returned:", result)
print("-" * 40)

# Test case 2: Binary number 1000 = Decimal number 8
linked_list = LinkedList(1)
linked_list.append(0)
linked_list.append(0)
linked_list.append(0)
print("Test case 2 linked list:")
linked_list.print_list()
result = linked_list.binary_to_decimal()
try:
    assert result == 8
    print("Test case 2 passed, returned:", result)
except AssertionError:
    print("Test case 2 failed, returned:", result)
print("-" * 40)

# Test case 3: Binary number 0 = Decimal number 0
linked_list = LinkedList(0)
print("Test case 3 linked list:")
linked_list.print_list()
result = linked_list.binary_to_decimal()
try:
    assert result == 0
    print("Test case 3 passed, returned:", result)
except AssertionError:
    print("Test case 3 failed, returned:", result)
print("-" * 40)

# Test case 4: Binary number 1 = Decimal number 1
linked_list = LinkedList(1)
print("Test case 4 linked list:")
linked_list.print_list()
result = linked_list.binary_to_decimal()
try:
    assert result == 1
    print("Test case 4 passed, returned:", result)
except AssertionError:
    print("Test case 4 failed, returned:", result)
print("-" * 40)

# Test case 5: Binary number 1101 = Decimal number 13
linked_list = LinkedList(1)
linked_list.append(1)
linked_list.append(0)
linked_list.append(1)
print("Test case 5 linked list:")
linked_list.print_list()
result = linked_list.binary_to_decimal()
try:
    assert result == 13
    print("Test case 5 passed, returned:", result)
except AssertionError:
    print("Test case 5 failed, returned:", result)
print("-" * 40)

    
 
"""
    EXPECTED OUTPUT:
    ----------------
    Test case 1 linked list:
    1 -> 1 -> 0
    Test case 1 passed, returned: 6
    ----------------------------------------
    Test case 2 linked list:
    1 -> 0 -> 0 -> 0
    Test case 2 passed, returned: 8
    ----------------------------------------
    Test case 3 linked list:
    0
    Test case 3 passed, returned: 0
    ----------------------------------------
    Test case 4 linked list:
    1
    Test case 4 passed, returned: 1
    ----------------------------------------
    Test case 5 linked list:
    1 -> 1 -> 0 -> 1
    Test case 5 passed, returned: 13
"""