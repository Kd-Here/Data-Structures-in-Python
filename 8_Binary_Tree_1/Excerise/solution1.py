# https://pythontutor.com/render.html#code=class%20BinarySearchTree%3A%0A%20%20%20%20def%20__init__%28self,data%29%20-%3E%20None%3A%0A%20%20%20%20%20%20%20%20self.data%20%3D%20data%20%0A%20%20%20%20%20%20%20%20self.right%20%3D%20None%20%0A%20%20%20%20%20%20%20%20self.left%20%3D%20None%0A%0A%20%20%20%20def%20search%28self,%20value%29%3A%0A%20%20%20%20%20%20%20%20if%20self.data%20%3D%3D%20value%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20return%20%22Value%20present%20in%20the%20BST.%22%0A%0A%20%20%20%20%20%20%20%20elif%20value%20%3C%20self.data%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20if%20self.left%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20return%20self.left.search%28value%29%20%20%23%20Notice%20the%20return%20here%0A%20%20%20%20%20%20%20%20%20%20%20%20else%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20return%20%22Value%20not%20present%20in%20the%20BST.%22%0A%0A%20%20%20%20%20%20%20%20elif%20value%20%3E%20self.data%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20if%20self.right%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20return%20self.right.search%28value%29%20%20%23%20Notice%20the%20return%20here%0A%20%20%20%20%20%20%20%20%20%20%20%20else%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20return%20%22Value%20not%20present%20in%20the%20BST.%22%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%0A%0A%20%20%20%20%20%20%20%20%0A%0A%20%20%20%20def%20add_child%28self,data%29%3A%0A%20%20%20%20%20%20%20%20if%20data%20%3D%3D%20self.data%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20return%0A%20%20%20%20%20%20%20%20%0A%20%20%20%20%20%20%20%20if%20data%20%3C%20self.data%3A%20%20%20%20%20%20%20%20%20%20%20%23add%20to%20left%20child%0A%20%20%20%20%20%20%20%20%20%20%20%20if%20self.left%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20self.left.add_child%28data%29%0A%0A%20%20%20%20%20%20%20%20%20%20%20%20else%3A%20%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20newnode%20%3D%20BinarySearchTree%28data%29%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20self.left%20%3D%20newnode%0A%0A%20%20%20%20%20%20%20%20else%3A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%23add%20to%20right%20child%0A%20%20%20%20%20%20%20%20%20%20%20%20if%20self.right%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20self.right.add_child%28data%29%0A%20%20%20%20%20%20%20%20%20%20%20%20else%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20newnode%20%3D%20BinarySearchTree%28data%29%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20self.right%20%3D%20newnode%0A%0A%0A%20%20%20%20def%20post_ord%28self,%20ele%3DNone%29%3A%0A%20%20%20%20%20%20%20%20if%20ele%20is%20None%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20ele%20%3D%20%5B%5D%0A%0A%20%20%20%20%20%20%20%20if%20self.left%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20self.left.post_ord%28ele%29%20%20%23%20Recursively%20traverse%20the%20left%20subtree%0A%0A%20%20%20%20%20%20%20%20if%20self.right%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20self.right.post_ord%28ele%29%20%20%23%20Recursively%20traverse%20the%20right%20subtree%0A%0A%20%20%20%20%20%20%20%20ele.append%28self.data%29%20%20%23%20Visit%20the%20current%20node%20%28root%29%0A%0A%20%20%20%20%20%20%20%20return%20ele%0A%20%20%20%20%20%20%20%20%0A%0A%0A%0Adef%20generate_tree%28li%29%3A%0A%20%20%20%20root%20%3D%20BinarySearchTree%28li%5B0%5D%29%0A%20%20%20%20%0A%20%20%20%20for%20i%20in%20range%281,len%28li%29%29%3A%0A%20%20%20%20%20%20%20%20root.add_child%28li%5Bi%5D%29%0A%20%20%20%20return%20root%0A%20%20%20%20%20%20%20%20%0A%0Anumbers_tree%20%3D%20generate_tree%28%5B17,%204,%201,%2020,%209,%2023,%2018,%2034%5D%29%0Aprint%28numbers_tree.post_ord%28%29%29&cumulative=false&curInstr=160&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false

class BinarySearchTree:
    def __init__(self,data) -> None:
        self.data = data 
        self.right = None 
        self.left = None

    def search(self, value):
        if self.data == value:
            return "Value present in the BST."

        elif value < self.data:
            if self.left:
                return self.left.search(value)  # Notice the return here
            else:
                return "Value not present in the BST."

        elif value > self.data:
            if self.right:
                return self.right.search(value)  # Notice the return here
            else:
                return "Value not present in the BST."
                    

        

    def add_child(self,data):
        if data == self.data:
            return
        
        if data < self.data:           #add to left child
            if self.left:
                self.left.add_child(data)

            else: 
                newnode = BinarySearchTree(data)
                self.left = newnode

        else:                          #add to right child
            if self.right:
                self.right.add_child(data)
            else:
                newnode = BinarySearchTree(data)
                self.right = newnode


    def post_ord(self, ele=None):
        if ele is None:
            ele = []

        if self.left:
            self.left.post_ord(ele)  # Recursively traverse the left subtree

        if self.right:
            self.right.post_ord(ele)  # Recursively traverse the right subtree

        ele.append(self.data)  # Visit the current node (root)

        return ele
        



def generate_tree(li):
    root = BinarySearchTree(li[0])
    
    for i in range(1,len(li)):
        root.add_child(li[i])
    return root
        

numbers_tree = generate_tree([17, 4, 1, 20, 9, 23, 18, 34])
print(numbers_tree.post_ord())



