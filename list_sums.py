"""1. Python program to calculate the sum of a list of numbers."""

def recusrive_sum(n):
    if len(n) == 0:
        return 0
    k = n.pop()
    return k + recusrive_sum(n)
    



# print(recusrive_sum([2, 4, 5, 6, 7]))

"""Alternatively """

def recusrive_sum_2(n):
    if len(n) == 0:
        return n
    return n[0] + recusrive_sum(n[1:])
    
print(recusrive_sum_2([2, 4, 5, 6, 7]))
