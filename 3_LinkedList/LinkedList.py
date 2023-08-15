class Node:
    def __init__(self, value, address=None):
        self.value = value
        self.address = address

class LinkedList:
    def __init__(self, *data):
        if len(data) == 0:
            self.head = None
        else:
            self.head = Node(data[0])
            current_node = self.head

            for i in range(1, len(data)):
                new_node = Node(data[i])
                current_node.address = new_node
                current_node = new_node
            
    
    def __str__(self) -> str:
        i = self.head
        while i is not None:
            print(i.value,end="")
            i = i.address
            if i is None:
                return f" "
            print(end=" -> ")
        return " " #Since you used dungen method it will have return so i'm just returning balnk space

    """
    This is only appending assuming linkedlist have atleast 1 element
    """
    def append(self,nvalue) :
        f1n = self.head
        while f1n is not None:
            # print(f1n.value,f1n.address)
            lastobj = f1n     #This lastobj is created to store the Node which is the last in previous linkedlist bcoz think why it's here not 1 line after 
            f1n = f1n.address   
        NewNode = Node(nvalue)
        lastobj.address = NewNode
        NewNode.address = None


    """
    This method insert will insert a new node after the given index handles only to size less then given data, can't insert at head If need you can do also
    """
    def insert(self,nposition,nvalue):
        fn = self.head
        lcount = 1

        while fn is not None:
            if lcount == nposition:
                new_inserted_node = Node(nvalue,fn.address)       #First creating new inserted node of nvalue 
                # new_inserted_node.address = fn.address #In new inserted node address we give refference of it's next node in linkedlist i.e node that will be following the current node if there was no inserted node
                fn.address = new_inserted_node         #In address of previous node of inserted node we put refference for new inserted node

            lcount += 1
            fn = fn.address   


    """
    This method will delete the node at given index exception occur at first and last position
    """
    def delete(self,nposition):
        fn =self.head
        lcount = 1

        while fn is not None:
            if lcount == nposition-1:
                storing = fn
            elif lcount == nposition:
                storing.address = fn.address
            lcount += 1
            fn = fn.address   




linklist = LinkedList(2, 3, 4, 5, 6, 7, 8)
print(linklist)

linklist.append(9)
print(linklist)

linklist.insert(1,9899)
print(linklist)


linklist.delete(2)
print(linklist)

linklist.delete(7)
print(linklist)






""""
This is code from gpt optimize for all exception condition!
"""

'''class Node:
    def __init__(self, value, address=None):
        self.value = value
        self.address = address

class LinkedList:
    def __init__(self, *data):
        if len(data) == 0:
            self.head = None
        else:
            self.head = Node(data[0])
            current_node = self.head

            for i in range(1, len(data)):
                new_node = Node(data[i])
                current_node.address = new_node
                current_node = new_node
            
    def __str__(self) -> str:
        i = self.head
        while i is not None:
            print(i.value, end="")
            i = i.address
            if i is None:
                return f" "
            print(end=" -> ")
        return " "

    def append(self, nvalue):
        f1n = self.head
        while f1n is not None:
            lastobj = f1n
            f1n = f1n.address
        new_node = Node(nvalue)
        lastobj.address = new_node
        new_node.address = None

    def insert(self, nposition, nvalue):
        if nposition == 0:
            new_node = Node(nvalue)
            new_node.address = self.head
            self.head = new_node
            return
        
        fn = self.head
        lcount = 1

        while fn is not None:
            if lcount == nposition:
                new_inserted_node = Node(nvalue)
                new_inserted_node.address = fn.address
                fn.address = new_inserted_node
                return
            lcount += 1
            fn = fn.address

    def delete(self, nposition):
        if nposition == 0:
            self.head = self.head.address
            return

        fn = self.head
        lcount = 1

        while fn is not None:
            if lcount == nposition - 1:
                fn.address = fn.address.address
                return
            lcount += 1
            fn = fn.address

'''