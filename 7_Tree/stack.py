from collections import deque

class STACK:
    def __init__(self) -> None:
        self.stack = deque()

    def push(self,element):
        self.stack.append(element)
    
    def pop(self):
        if len(self.stack) >0:
            a =  self.stack.pop()
            return a
        else:
            raise Exception("Popping from empty list")

    # Returns the top most or last pushed element
    def peek(self): 
        return self.stack[-1]

    def size(self):
        return len(self.stack)


if __name__ == "__main__":
    s = STACK()
    s.push(1)
    s.push(2)
    s.push(3)
    s.push("A")
    if "A" in s.stack:
        s.pop()
    print(s.stack)