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




    def in_order(self):
        """
        Perform an in-order traversal on the BST.
        
        In an in-order traversal, the left subtree of a node is traversed first, 
        followed by the node itself, and then its right subtree. 
        This results in visiting all nodes in ascending order for a BST.
        
        Returns:
            elements (List[int]): A list of integers representing the nodes 
                                in ascending order.
        """
        
        # Initialize an empty list to hold the nodes in the traversal order.
        elements = []
        
        # If there's a left child, traverse its subtree first.
        if self.left:
            elements += self.left.in_order()  # Recursively traverse the left subtree.
            print(elements)

        # Visit the current node (i.e., add the current node's data to the list).
        elements.append(self.data)
        
        # If there's a right child, traverse its subtree.
        if self.right:
            print(elements)
            elements += self.right.in_order()  # Recursively traverse the right subtree.

        # Return the list of nodes in ascending order.
        return elements



def generate_tree(li):
    root = BinarySearchTree(li[0])
    
    for i in range(1,len(li)):
        root.add_child(li[i])
    return root
        

root = BinarySearchTree(9)
root.add_child(10)
root.add_child(4)
root.add_child(5)
root.add_child(11)
root.add_child(13)
root.add_child(11)

# c = root.in_order() #Inoder see used for sorting and as a set repeated are not present
# print(c)

numbers_tree = generate_tree([17, 4, 1, 20, 9, 23, 18, 34])
print(numbers_tree.in_order())



countries = ["India","Pakistan","Germany", "USA","China","India","UK","USA"]
country_tree = generate_tree(countries)

print("UK is in the list? ", country_tree.search("UK"))
print("Sweden is in the list? ", country_tree.search("Sweden"))
