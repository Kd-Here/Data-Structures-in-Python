def fib(n):
    if n == 1:
        return 1
    elif n == 0:
        return 0
    
    else:
        return fib(n-1) + fib(n-2)


n = int(input("Enter number to see fibonacci till that position: "))
for i in range(n):
    c = fib(i)
    print(c)