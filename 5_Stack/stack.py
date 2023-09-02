class Stack:
    def __init__(self) -> None:
        self.stack = []
        self.top = len(self.stack)
    
    def push(self,insert):
        self.stack.append(insert)
        self.top = len(self.stack)
    
    def pop(self):
        if self.top >0:
            self.stack.pop()
            self.top = len(self.stack)
        else:
            raise Exception('Poping from empty stack')
    
    def peek(self):
        return self.stack[self.top-1]



S = Stack()
S.push(1)
S.push(232)
S.push(2)
S.push(243)
S.push(343)
# print(S.peek())
S.pop()
S.pop()
# print(S.stack)


'''
List in python initailly has capacity and as u reach capacity it increases.
The issue with using a list as a stack is that list uses dymanic array internally 
and when it reaches its capacity it will reallocate a big chunk of memory somewhere else 
in memory area and copy all the elements. 
For example in below diagram if a list has a capacity of 10 and we try to insert 11th element, 
it will not allocate new memory in a different memory region, 
copy all 10 elements and then insert the 11th element. 
So overhead here is (1) allocate new memory plus (2) copy all existing elements in new memory area
To solve this problem we use deque which is double ended queue. It uses doubly-linked list!
'''



from collections import deque

class STACK:
    def __init__(self) -> None:
        self.stack = deque()

    def push(self,element):
        self.stack.append(element)
    
    def pop(self):
        if len(self.stack) >0:
            self.stack.pop()
        else:
            raise Exception("Popping from empty list")

    # Returns the top most or last pushed element
    def peek(self): 
        return self.stack[-1]


if __name__ == '__main__':
    S = STACK()
    print(dir(S))
    S.push(1)
    S.push(2)
    S.push(3)
    S.pop()
    print(S.peek())
    print(S.stack)

