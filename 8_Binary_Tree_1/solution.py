from collections import deque 

class BinarySearchTree:
    def __init__(self,data) -> None:
        self.data = data
        self.left = None
        self.right = None
    
    def add_child(self,data):
        if self.data > data:
            newnode = BinarySearchTree(data)
            if self.left:
                 self.left.add_child(data)
            else:
                self.left = newnode
        else:
            newnode = BinarySearchTree(data)
            if self.right:
                 self.right.add_child(data)
            else:
                self.right = newnode


    def search(self,search_data):
        if self.data == search_data:
            return "Got the data"
        
        elif self.data > search_data: # left
            if self.left:
                self.left.search(search_data)
            else:
                print("Element should present in right half but not found")
                return 
        
        else:
            if self.right:
                self.right.search(search_data)
            else:
                print("Element should present in left half but not found")
                return 


    def in_order(self):
        self.stack = deque()
        s = self.stack

        s.append(self)
        visited = []
        while len(s) > 0:
            
            if self.left and self.left not in visited:
                visited.append(self.left)
                s.append(self.left)
                self = self.left   #Making child as current node it will get iterated to  find it has left or right

            elif self.right and self.right not in visited:
                c = s.pop()
                print(c.data)
                visited.append(self.left)
                s.append(self.right)
                self = self.right

            else:
                c = s.pop()
                print(c.data)
                if len(s)>0:
                    self = s[-1]

"""
Try to find optimised way you used stack and visited list use other approach next time and try
"""



        



root = BinarySearchTree(9)
root.add_child(10)
root.add_child(4)
root.add_child(5)
root.add_child(11)
root.add_child(13)

# root.search(99)


root.in_order()