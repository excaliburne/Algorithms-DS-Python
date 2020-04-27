class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None 
        self.prev = None
    
class LinkedList:
    def __init__(self):
        self.head = Node() #placeholder
    
    def append(self, data):
        new_node = Node(data)
        cur = self.head 
        while cur.next != None:
            cur = cur.next 
        cur.next = new_node
    
    def length(self):
        cur = self.head 
        total = 0
        while cur.next != None:
            total += 1
            cur = cur.next 
        return total 
    
    def display(self):
        elems = []
        cur_node = self.head 
        while cur_node.next != None:
            cur_node=cur_node.next
            elems.append(cur_node.data)
        print(elems)

    def get(self, index):
        if index >= self.length():
            print("ERROR: 'Get' index out of range")
            return None 
    
        cur_idx = 0
        cur_node = self.head
        while True:
            cur_node = cur_node.next
            if cur_idx == index: return cur_node.data
            cur_idx += 1

    def erase(self, index):
        if index >= self.length():
            print("ERROR: 'Get' index out of range")
            return 

        cur_idx = 0
        cur_node = self.head
        while True:
            last_node = cur_node
            cur_node = cur_node.next 
            if cur_idx == index:
                last_node.next = cur_node.next 
                return
            cur_idx += 1
    
    """ 
    def reverse_list(self):
        if not self.head or not self.head.next:
            return self.head
        prev = None
        while self.head:
            current = self.head
            head = self.head.next
            current.next = prev
            prev = current
        return prev

    """




my_list = LinkedList()

my_list.append(1)
my_list.append(2)
my_list.append(3)
my_list.append(4)

my_list.display()

print("element a 2nd index: {}".format(my_list.get(2)))





