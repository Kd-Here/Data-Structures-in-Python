class Node:
    def __init__(self,data) -> None:
        self.data = data
        self.children = []
        self.parent = None

    def add_child(self,child):
        child.parent = self
        self.children.append(child)

    def get_lvl(self):
        a = self.parent
        lvl = 0
        while a:
            lvl += 1
            a = a.parent
        return lvl


    def print_tree(self):
        if self.parent:
            print(self.get_lvl()*5*" "+"|"+self.get_lvl()*"-",end="")
        print(self.data)
        for i in self.children:
            i.print_tree()



if __name__ == "__main__":
    root = Node("Electronics")

    laptop = Node("Laptop")
    laptop.add_child(Node("Mac"))
    laptop.add_child(Node("Surface"))
    laptop.add_child(Node("Thinkpad"))

    cellphone = Node("Cell Phone")
    cellphone.add_child(Node("iPhone"))
    cellphone.add_child(Node("Google Pixel"))
    cellphone.add_child(Node("Vivo"))

    tv = Node("TV")
    tv.add_child(Node("Samsung"))
    tv.add_child(Node("LG"))

    root.add_child(laptop)
    root.add_child(cellphone)
    root.add_child(tv)

    root.print_tree()
