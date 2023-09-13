class TreeNode:
    def __init__(self, name,designation):
        self.name = name
        self.designation = designation
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


    def print_tree(self,show_hierarchy, prefix="", is_last=True):
        if show_hierarchy == "name":
            print(prefix + ("└─── " if is_last else "├─── ") + self.name)
        elif show_hierarchy == "designation":
            print(prefix + ("└─── " if is_last else "├─── ") + self.designation)
        else:
            print(prefix + ("└─── " if is_last else "├─── ") + self.name,self.designation)
        child_count = len(self.children)

        for index, child in enumerate(self.children):
            is_last_child = index == child_count - 1
            child.print_tree(show_hierarchy,prefix + ("    " if is_last else "│   "), is_last_child)


def build_management_tree():
    me = TreeNode("Nilupul","(CEO)")

    cto = TreeNode("Chinmay","(CTO)")
    m1 = TreeNode("Vishwa","(Infrastructure Head)")

    m1.add_child(TreeNode("Dhaval","(Cloud Manager)"))
    m1.add_child(TreeNode("Abhijit","(App Manager)"))

    cto.add_child(m1)
    cto.add_child(TreeNode("Aamir","(Application Head)"))

    n1 = TreeNode("Gels","(HR Head)")
    n1.add_child(TreeNode("Peter","(Recruitment Manager)"))
    n1.add_child(TreeNode("Waqas","(Policy Manager)"))

    me.add_child(cto)
    me.add_child(n1)


    return me
            
if __name__ == "__main__":
    root_node = build_management_tree()
    root_node.print_tree("name")   #prints only name hierarchy

    root_node.print_tree("designation") # prints only designation hierarchy
    root_node.print_tree("both") # prints both (name and designation) hierarchy
