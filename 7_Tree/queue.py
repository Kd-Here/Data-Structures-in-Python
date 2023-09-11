from collections import deque
class QUEUE:
    def __init__(self) -> None:
        self.q = deque()

    def enqueue(self,input):
        self.q.append(input)

    def dequeue(self):
        if len(self.q) > 0:
            c = self.q.popleft()
            return c

        else:
            raise Exception("Dequeuing from empty queue!")
    
    def size(self):
        return len(self.q)
    
    def __str__(self) -> str:
        return f"{str(self.q)}"
    
