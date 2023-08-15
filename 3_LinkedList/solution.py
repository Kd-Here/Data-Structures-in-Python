class Node:
    def __init__(self,data,address) -> None:
        self.data = data
        self.address = address


class LinkedList:
    def __init__(self) -> None:
        self.head = None

    def insert_at_beginning(self,data):
        n0 = Node(data,self.head)
        self.head = n0

    def print(self):
        if self.head == None:
            print("LinkedList is empty")
            return

        a = self.head
        lstr = " "
        while a is not None:
            lstr += str(a.data) + ' ==> ' if a.address else str(a.data)
            a = a.address
        print(lstr)

    def get_len(self):
        a = self.head
        count = 0
        while a is not None:
            count += 1
            a = a.address
        return count
    

    def insert_at_end(self,data):
        if self.head is None:
            self.head = Node(data,None)
            return

        a = self.head
        while a.address is not None:
            a = a.address
        a.address = Node(data,None)

    def insert_at(self,index,data):
        if index <0 and index > self.get_len():
            raise Exception("Invalid Index")

        elif index == 0:
            self.insert_at_beginning(data)
            return
        
        count = 0
        a = self.head
        while a is not None:
            if count == index-1:
                inserted_node = Node(data,a.address)
                a.address = inserted_node
                break
            a = a.address
            count += 1

    def remove_at(self,index):
        if index <0 and index > self.get_len():
            raise Exception("Invalid index for delete")
        
        elif index == 0:
            self.head = self.head.address
        
        count = 0
        a = self.head
        while a is not None:
            if count == index-1:
                a.address = a.address.address
            a = a.address
            count += 1

    def insert_after_value(self,data_after,data_to_insert):
        a = self.head
        while a is not None:
            if a.data == data_after:
                newnode = Node(data_to_insert,a.address)
                a.address = newnode
            a = a.address

    def remove_by_value(self,data):
        a = self.head
        count = 0
        while a is not None:
            if data == a.data :
                self.remove_at(count)
                break
            count +=1
            a = a.address


    def insert_values(self,datalist):
        self.head = None
        for i in datalist:
            self.insert_at_end(i)


if __name__ == "__main__":
    ll = LinkedList()
    ll.insert_values(["banana","mango","grapes","orange"])
    ll.print()
    ll.insert_after_value("mango","apple") # insert apple after mango
    ll.print()
    ll.remove_by_value("banana") # remove orange from linked list
    ll.print()

    
