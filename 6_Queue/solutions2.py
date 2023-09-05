# for i in range(1,11):
#     print(bin(i)[2:])


"""
from queue import QUEUE

q = QUEUE()
q1 = QUEUE()

def add_0(a):
    f = a+'0'
    q.enqueue(f)

def add_1(a):
    s = a +'1'
    q.enqueue(s)


def printing_Seq_0():
    f = (q.dequeue())
    q1.enqueue(f)
    print(f)

def printing_Seq_1():
    s = (q.dequeue())
    q1.enqueue(s)
    print(s)

print(1)

k = '1'
for i in range(1,5):
    add_0(k)
    printing_Seq_0()
    add_1(k)
    printing_Seq_1()
    k = q1.dequeue()

add_0(k)
printing_Seq_0()
"""


from queue import QUEUE


def decimal_binary_seq(n):
    q = QUEUE()
    c = '1'
    print(c)
    for i in range(n-1):
        f = c + '0'
        s = c +'1'
        q.enqueue(f)
        q.enqueue(s)
        c = q.dequeue()
        print(c)

decimal_binary_seq(10)