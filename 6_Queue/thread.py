import threading
import time

def my_function(a):
    for i in range(a):
        time.sleep(1)
        print(i)

def myfunction2(a):
    for i in a:
        time.sleep(1)
        print(i)
# Create and start a thread
my_thread = threading.Thread(target=my_function,args=(10,))
my_thread.start()

orders = ['pizza','samosa','pasta','biryani','burger']

my_thread2 = threading.Thread(target=myfunction2,args=(orders,))
my_thread2.start()