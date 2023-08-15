class Node:
    def __init__(self,data,next,prev) -> None:
        self.data = data
        self.next = next
        self.prev = prev

class Linkedlist:
    def __init__(self) -> None:
        self.head = None
    
    def insert_at_beginning(self,data):
        if self.head == None:
            node = Node(data,None,None)
            self.head = node
        else:
            node = Node(data,self.head,None)
            self.head.prev = node
            self.head = node

    def print_forward(self):
        i = self.head
        while i is not None:
            print(i.data)
            i = i.next

    def last_end(self):
        i = self.head
        while i.next is not None:
            i = i.next
        return i
    
    def print_backward(self):
        c = self.last_end()
        while c is not None:
            print(c.data)
            c = c.prev
    
    def get_len(self):
        count = 0
        a = self.head
        while a is not None:
            count += 1
            a = a.next
        return count
    
    def insert_at_end(self,data):
        if self.head == None:
            node = Node(data,None,None)
            self.head = node
        else:
            c = self.last_end()
            lnode = Node(data,None,c)
            c.next = lnode


    def insert_at(self,index,data):
        if index < 0 and index > self.get_len():
            raise Exception("Invalid Index")

        elif index == 0:
            self.insert_at_beginning(data)

        elif index == self.get_len():
            self.insert_at_end(data)

        else:
            i = self.head
            c = 0
            while i is not None:
                if c == index-1:            #This we are doing at earlier of index-1 node i.e insert node and make changes in address 

                    inserted_node = Node(data,i.next,i)
                    i.next.prev = inserted_node
                    i.next = inserted_node

                i = i.next
                c += 1


    def remove_at(self,index):
        if index < 0 and index > self.get_len():
            raise Exception("Invalid Index")

        elif index == 0:
            first = self.head
            self.head = first.next
            first.head = None

        elif index == self.get_len():
            last = self.last_end()
            last.prev.next = None  #For deleting last node it's previous node next address should none           

        else:
            current_node = self.head
            c = 0
            while current_node is not None:
                if c == index-1:            #This we are doing at earlier of index-1 node i.e  change it's next address 
                    k = current_node
                    k.next.next.prev = current_node
                    k.next = current_node.next.next

                current_node = current_node.next
                c += 1

    def insert_after_value(self,data_after,data_to_insert):
        i = self.head
        c = 0
        while i is not None:
            k = i
            if i.data == data_after:
                self.insert_at(c+1,data_to_insert)
            i = i.next
            c += 1

    # def insert_after_value(self,data_after,data_to_insert):
    #     i = self.head
    #     while i is not None:
    #         k = i
    #         if i.data == data_after:
    #             inserted_node = Node(data_to_insert,k.next,k)
    #             k.next.prev = inserted_node
    #             k.next = inserted_node
    #         i = i.next

    def remove_by_value(self,data):
        i = self.head
        c = 0
        while i is not None:
            if i.data == data:
                self.remove_at(c)
            i = i.next
            c += 1





l = Linkedlist()
l.insert_at_beginning(124)
l.insert_at_beginning(123)
l.insert_at_beginning(121)
l.insert_at_beginning(120)
l.insert_at_end(125)
print("Forward & Backward")
l.print_forward()
print("========================================")
l.print_backward()


print("========================================")
print("Size of Double-LinkedList is",l.get_len())

l.insert_at(2,122)
l.remove_at(2)
print("Printing after remove operation @ index 2")
l.print_forward()
print("========================================")
l.print_backward()


print("========================================")
print("Printing after inserting 122 after 121 ")
l.insert_after_value(121,122)
l.print_forward()


print("========================================")
print("Printing after removing 122 ")
l.remove_by_value(122)
l.print_backward()