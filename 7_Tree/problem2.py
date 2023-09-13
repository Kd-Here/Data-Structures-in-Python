class TreeNode:
    def __init__(self,data) -> None:
        self.data = data
        self.children = []
        self.parent = None

    def add_child(self,child):
        child.parent = self
        self.children.append(child)

    def get_lvl(self,required_lvl = None):
        a = self.parent
        lvl = 0
        while a:
            if lvl == required_lvl:
                return False
            lvl += 1
            a = a.parent
        return lvl

    def print_tree(self,lvl):
        if self.parent:
            if self.get_lvl(lvl):
                print(self.get_lvl()*5*" "+"|"+self.get_lvl()*"-",end="")
                print(self.data)
        else:
            print(self.data)

        for i in self.children:
            i.print_tree(lvl)




if __name__ == "__main__":
    root = TreeNode("Global")

    india = TreeNode("India")

    maharashtra  = TreeNode("Maharashtra")
    maharashtra.add_child(TreeNode("Mumbai"))
    maharashtra.add_child(TreeNode("Thane"))
    maharashtra.add_child(TreeNode("Pune"))
    maharashtra.add_child(TreeNode("Nagpur"))
    maharashtra.add_child(TreeNode("Nashik"))
    maharashtra.add_child(TreeNode("Kolhapur , Satra"))


    gujarat = TreeNode("Gujarat")
    gujarat.add_child(TreeNode("Ahmedabad"))
    gujarat.add_child(TreeNode("Baroda"))

    karnataka = TreeNode("Karnataka")
    karnataka.add_child(TreeNode("Bangluru"))
    karnataka.add_child(TreeNode("Mysore"))

    india.add_child(maharashtra)
    india.add_child(gujarat)
    india.add_child(karnataka)

    usa = TreeNode("USA")

    ny = TreeNode("New York")
    ny.add_child(TreeNode("NYC"))
    ny.add_child(TreeNode("Buffalo"))
    ny.add_child(TreeNode("Brooklyn"))
    ny.add_child(TreeNode("Central Square"))
    ny.add_child(TreeNode("Manhattan"))
    ny.add_child(TreeNode("Queens , Lake View"))


    nj = TreeNode("New Jersey")
    nj.add_child(TreeNode("Princeton"))
    nj.add_child(TreeNode("Trenton"))

    california = TreeNode("California")
    california.add_child(TreeNode("San Francisco"))
    california.add_child(TreeNode("Mountain View"))
    california.add_child(TreeNode("Palo Alto"))

    usa.add_child(ny)
    usa.add_child(nj)
    usa.add_child(california)

    root.add_child(india)
    root.add_child(usa)

    root.print_tree(3)