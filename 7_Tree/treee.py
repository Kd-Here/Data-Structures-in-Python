'''class Node:
    def __init__(self,data,) -> None:
        self.data = data
        self.child = []
    

class Tree:
    def __init__(self) -> None:
        self.root = None

    def set_root_node(self,data):
        self.root = Node(data)

    def set_node_level(self,node_number):
        a = self.root
        for i in range(node_number):
            if len(a.child) == 0:
                raise Exception("Not having child to it") 
            k = a.child[0]
            a = k
        return a 
            

    def add_child_to_node(self,data,node_address=None):
        if node_address:
            c1 = Node(data)
            node_address.child.append(c1)
        else:
            c1 = Node(data)
            self.root.child.append(c1)

    def printing_childs(self):
        print(self.root.data)
        s = self.root.child
        for i in s:
            print(i.data)
            

t = Tree()
t.set_root_node("Electronic")
t.add_child_to_node('Mobile')
t.add_child_to_node('SmartWatch')
t.add_child_to_node('Earphones')


c = t.set_node_level(1)
print(c.data)
t.add_child_to_node("Iphone",c)

# t.printing_childs()


s = t.set_node_level(2)
t.add_child_to_node("Iphone 15",s)


k = t.set_node_level(3)
# print("K",k.data)
# k = t.set_node_level(4)

'''

from queue import QUEUE
from stack import STACK
class Node:
    def __init__(self, data):
        self.data = data
        self.children = []

class Tree:
    def __init__(self, root): 
        self.root = Node(root)

    # Created add_child using bfs approach

    def add_child(self, parent, child_data):
        r = self.root
        if r.data == parent:
            node = Node(child_data)
            r.children.append(node)

        else:

            q = QUEUE()
            def add_children_to_queue(a):
                for i in a:
                    q.enqueue(i)
            
            add_children_to_queue(r.children)
            while q.size() > 0:
                c = q.dequeue()
                if c.data == parent:
                    n1 = Node(child_data)  
                    c.children.append(n1)      
                    break
                else:
                    add_children_to_queue(c.children)


    def remove_child(self, parent, child_data):
        if self.root.data == parent:
            for i in self.root.children:
                if i.data == child_data:
                    self.root.children.remove(i)
                    return

        else:
            q = QUEUE()
            def add_child_to_queue(a):
                for i in a:
                    q.enqueue(i)


            add_child_to_queue(self.root.children)

            
            while q.size() > 0:
                r = q.dequeue()
                if r.data == parent:
                    for i in r.children:
                        if i.data == child_data:
                            r.children.remove(i)
                    
                else:
                    add_child_to_queue(r.children)

    def traverse_in_order(self):
        # Order is Washington, D, Deroit, A, Chicago, C, Canbera.
        print("The in-order-transversal is :- Left,Root,Right")
        s = STACK()
        s.push(self.root)

        a = self.root
        visited_node_list =[] #For optimisation you can check if node in stack or not | This will not possible with this apporach since we removing i.e. pop() and can't keep track of removed using stack
        while s.size() > 0:

            if len(s.peek().children) > 0 and s.peek().children[0] not in visited_node_list :
                visited_node_list.append(s.peek().children[0])
                s.push(s.peek().children[0])


            elif len(s.peek().children) > 1 and s.peek().children[1] not in visited_node_list:
                k = s.peek()
                print(k.data," ",end=" ")
                s.pop()
                visited_node_list.append(k.children[1])
                s.push(k.children[1])     

            else:
                k = s.pop()
                print(k.data," ",end=" ")


T = Tree("A")   
T.add_child("A","D")
T.add_child("A","C")
T.add_child("D","Washington")
T.add_child("D","Deroit")
T.add_child("C","Chicago")
T.add_child("C","Canbera")


T.traverse_in_order()
# Remember you solved backtracking difficulty

# print(T.root.children[0].children[0].children)