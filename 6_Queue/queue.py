class Queue:
    def __init__(self) -> None:
        self.q = []
    

    # Enqueue is same as insertion | append 
    def enqueue(self,input):
        self.q.append(input)

    # Dequeue is same as pop from front side
    def dequeue(self):
        if self.size() > 0:
            c = self.q.pop(0)
            print(f"{c}")
        else:
            raise Exception("Empty queue")
    
    def size(self):
        return len(self.q)


'''
When working with queues in Python, one might be tempted to use the built-in list
due to its simplicity and familiarity. 
However, this choice is accompanied by challenges regarding performance and efficiency. 
In Python, a list starts with an initial capacity. Once you fill this capacity, as more elements are enqueued, 
the list expands dynamically. 
The drawback here is that this list, built on a dynamic array, 
reallocates a larger chunk of memory elsewhere when its current capacity is exhausted. 
This means, if you have a queue built on a list with a capacity of 10, and you enqueue an 11th element, 
it will first allocate a new memory chunk, copy all 10 existing elements to this new location, and then add the 11th element. 
This introduces two main inefficiencies: the allocation of new memory and copying the existing elements.

'''



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
    


if __name__ == "__main__":
    k = QUEUE()
    k.enqueue({
        'company': 'Wall Mart',
        'timestamp': '15 apr, 11.01 AM',
        'price': 131.100
    })
    k.enqueue({
        'company': 'D Mart',
        'timestamp': '15 apr, 11.02 AM',
        'price': 131.104
    })
    k.enqueue({
        'company': 'ebay',
        'timestamp': '15 apr, 11.03 AM',
        'price': 131.103
    })
    print(k.size())
    print(k.dequeue())
    print(k.q)

