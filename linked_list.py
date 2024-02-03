class Node:
    def __init__(self, data = None, next_node = None):
        self.data = data
        self.next_node = next_node

class LinkedList:
    def __init__(self):
        self.head = None
        self.last_node = None

    def to_list(self):
        l = []
        if self.head is None:
            return l

        node = self.head
        while node:
            l.append(node.data)
            node = node.next_node
        return l

    def print_ll(self):
        ll_string = ""
        node = self.head
        if node == None:
            print(None)
        while node:   # this means iterate till node is not None
            ll_string += f" {str(node.data)} ->"
            node = node.next_node
        
        ll_string += f" None"
        print(ll_string)

    '''If you don't keep track of last node from the start i.e. while adding new nodes from start of formation of LinkedList
    you have to iterate through whole linked list just for the first time when you want to add node at the end 
    Below is the code for that'''
    # def insert_beginning(self,data):
    #     new_node = Node(data,self.head)
    #     self.head = new_node

    # def insert_at_end(self,data):
    #     if self.head is None:
    #         self.insert_beginning(data)

    #     if self.last_node is None:
    #         print("Last Node is None")
    #         node = self.head
    #         while node.next_node:
    #             print('iter',node.data)
    #             node = node.next_node
            
    #         node.next_node = Node(data,None)
    #         self.last_node = node.next_node
    #     else:
    #         self.last_node.next_node = Node(data,None)
    #         self.last_node = self.last_node.next_node

    def insert_beginning(self,data):
        if self.head is None:
            self.head = Node(data,None)
            self.last_node = self.head

        new_node = Node(data,self.head)
        self.head = new_node

    def insert_at_end(self,data):
        if self.head is None:
            self.insert_beginning(data)

        self.last_node.next_node = Node(data,None)
        self.last_node = self.last_node.next_node

    def get_user_by_id(self,user_id):
        node = self.head
        while node:
            if node.data["id"] == int(user_id):
                return node.data
            node = node.next_node
        return None 



ll = LinkedList()

# Uncomment below to print Linked List
''' 
node4 = Node("Data4",None)
node3 = Node("Data3",node4)
node2 = Node("Data2",node3)
node1 = Node("Data1",node2)

ll.head = node1
ll.print_ll()   
'''

# Uncomment below to test insert at beginning
'''
ll.insert_beginning("data1")
ll.insert_beginning("data2")
ll.print_ll()
'''

# Uncomment below code to test and it can also be test with commented insert codes in LinkedList class.
'''
ll.insert_beginning("data1")
ll.insert_beginning("data1")
ll.insert_beginning("data1")
ll.insert_beginning("data1")
ll.insert_beginning("data1")
ll.insert_beginning("data1")
ll.insert_beginning("data1")
ll.insert_beginning("data1")
ll.insert_beginning("data1")
ll.insert_beginning("data1")

ll.insert_at_end("END")
ll.print_ll()
'''