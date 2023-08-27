class Node:
    def __init__(self,key,value,address = None) -> None:
        self.key = key
        self.value = value
        self.address = address

class LinkedList:
    def __init__(self) -> None:
        self.head = None

    def append(self,*data):
        if self.head == None:
            newnode = Node(data[0],data[1],None)
            self.head = newnode
        else:
            i = self.head
            while i is not None:
                previous_node = i
                i = i.address
            previous_node.address = Node(data[0],data[1],None)

    def retrive_value(self,index):
            i = self.head
            while i is not None:
                if i.key == index:
                    return i.value
                i = i.address
            else:
                return "Index not stored in dict"
        
    def index_present(self,*data):
        i = self.head
        c = 0
        while i is not None:
            if i.key == data[0]:
                i.value = data[1]
                return 1
            i = i.address
        
               
            
    def printing(self):
        i = self.head
        while i is not None:
            print(i.key,i.value,end=" -> ")
            i = i.address
        

class Dictionari:
    def __init__(self,data=None) -> None:
        self.data = [None] * 4
        self.count = 0
        # initializing a list of LinkedList objects for each bucket. This approach ensures we have a linked list ready to store key-value pairs for each bucket.
        self.bucket = [LinkedList() for i in range(5)]


    def hashvalue(self,input):
        a = sum (ord(i) for i in input)
        bucketindex = (a%3)
        return bucketindex
        # Here bucket should be 4 size but 1 extra more all rest modulus vlaue

    def __setitem__(self,index,value): 
        bucketindex = (self.hashvalue(index))

        # In bucket the linkedlist is present only create new node when index is not same if index is present earlier replace the value in that 
        if self.bucket[bucketindex].index_present(index,value) == None:
            self.bucket[bucketindex].append(index,value)


        # Now implemenatation of Linkedlist ie. collision avoidance        
     
    def __getitem__(self,index):
        bucketindex = self.hashvalue(index)
        return self.bucket[bucketindex].retrive_value(index)



K = Dictionari()
# This all __set__
K['march 1'] = 123
K['march 2'] = 456
K['march 3'] = 789
K['march 4'] = 234
K['march 5'] = 567
K['march 6'] = 890
K['march 7'] = 321
K['march 8'] = 654
K['march 9'] = 987
K['march 10'] = 432
K['march 11'] = 765
K['march 12'] = 198
K['march 13'] = 543
K['march 14'] = 876
K['march 15'] = 209
K['march 16'] = 654
K['march 17'] = 987
K['march 18'] = 123
K['march 19'] = 456
K['march 20'] = 789
K['march 21'] = 234
K['march 22'] = 567
K['march 23'] = 890
K['march 24'] = 321
K['march 25'] = 654
K['march 26'] = 987
K['march 27'] = 432
K['march 28'] = 765
K['march 29'] = 198
K['march 30'] = 543
K['march 31'] = 876

K['march 30'] = 535
K['march 29'] = 536
print(K.bucket[3].printing())

# This all __get__
# print
