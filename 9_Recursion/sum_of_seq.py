# n+(n-2)+(n-4)... (until n-x =< 0)
# Here we find common difference d is -2 
# Remember ap of std 9 formula try s of 50 numbers formula with here i.e a = n and d = n-4-(n-2)


def sum_of_sequence(n):
    if n<0:
        return 0
    return n + sum_of_sequence(n-2)

a = sum_of_sequence(10)
print(a)