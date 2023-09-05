import threading
import time

from queue import QUEUE

print("Welcome to Kd HOtel")


q = QUEUE()
def place_order(ord):
    for i in ord:
        q.enqueue(i)
        print("order placed Is:",i)
        time.sleep(0.5)

def serve_order():
    time.sleep(1)
    while q.size() > 0  :
        c = q.dequeue()
        print("order served Is:",c)
        time.sleep(2)


orders = ['pizza','samosa','pasta','biryani','burger']

place_order_thread = threading.Thread(target=place_order,args=(orders,)) #Here orders, are passed like this as tuple in python while passing args separtetly they are treated as tuple
serve_order_thread = threading.Thread(target=serve_order) #Be careful you are passing refference to function not calling the function i.e. end with()
place_order_thread.start()
serve_order_thread.start()