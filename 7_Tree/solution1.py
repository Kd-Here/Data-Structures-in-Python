class TreeNode:
    def __init__(self, data):
        self.data = data
        self.parent = None
        self.children = []

    def get_level(self):
        lvl = 0
        p = self.parent
        while p:
            lvl += 1
            p = p.parent
        return lvl


    def add_child(self,child_node):
        child_node.parent = self
        self.children.append(child_node)

    # def printing_Tree(self):
    #     if self.get_level():
    #         if self.get_level() > 1:
    #             print("│"+"           "+"└───"+"───"*self.get_level(),self.data)
    #         else:
    #             print("└───"+"───"*self.get_level(),self.data)
    #     else: 
    #         print(self.data)
    #     for i,j in enumerate(self.children):
    #         j.printing_Tree()

    def printing_Tree(self, prefix="", is_last=True):
        print(prefix + ("└─── " if is_last else "├─── ") + self.data)
        child_count = len(self.children)
        for index, child in enumerate(self.children):
            is_last_child = index == child_count - 1
            child.printing_Tree(prefix + ("    " if is_last else "│   "), is_last_child)

            
if __name__ == "__main__":
    root = TreeNode("Electronics")

    laptop = TreeNode("Laptop")
    laptop.add_child(TreeNode("Mac"))
    laptop.add_child(TreeNode("Surface"))
    laptop.add_child(TreeNode("Thinkpad"))



    cellphone = TreeNode("Cell Phone")
    cellphone.add_child(TreeNode("Google Pixel"))
    cellphone.add_child(TreeNode("Vivo"))
    tv = TreeNode("TV")
    tv.add_child(TreeNode("Samsung"))
    tv.add_child(TreeNode("LG"))

    root.add_child(laptop)
    root.add_child(cellphone)
    root.add_child(tv)
    
    root.printing_Tree()