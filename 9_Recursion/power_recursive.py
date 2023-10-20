# (power(3,4) -> 81


def power_re(a,b):
    if b == 0:
        return 1
    return a * power_re(a,b-1)

a = power_re(0,1)
print(a)