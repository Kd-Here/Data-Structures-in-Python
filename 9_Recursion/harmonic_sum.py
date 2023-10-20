# The harmonic sum is the sum of reciprocals of the positive integers.

def harmonic_sum(n):
    if n == 0:
        return 0
    return 1/n + harmonic_sum(n-1)

a = harmonic_sum(4)
print(a)