# # write recursion function for 2 to the power x
# when x = 1 y = 2
# x = 2 y = 4
# x = 3 y = 8
# every new is double of earlier

def power_recursion(n,a):
    if n == 1:
        return a
    return a*power_recursion(n-1,a)

print("this is a cubic function!")
for i in range(1,20):
    c = power_recursion(3,i)
    print("X = {} , Y = {}".format(i,c))