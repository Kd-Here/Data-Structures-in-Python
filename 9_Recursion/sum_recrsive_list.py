"""
Write a Python program to sum recursion lists.
Test Data: [1, 2, [3,4], [5,6]]
Expected Result: 21
"""

def recusrive_sum(n):
    if len(n) == 0:
        return 0
    k = n.pop()
    
    if type(k) == list:
        k = recusrive_sum(k)
    
    return k + recusrive_sum(n)
    
print( recusrive_sum([1, 2, [3,4],[5,6]]))
