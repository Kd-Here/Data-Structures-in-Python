# A a geometric series is a series with a constant ratio between successive terms.
# Considering this series 1, 1/2,   1/4
# a = 1, r = 1/2
# earlier I taught of     return (1/2) * geometric_series(n-1) but this will multiple 1/2 with n times we 1/2 , 1/4, 1/8



def geometric_series(n):
    if n == 0:
        return 1
    return pow((1/2),n) + geometric_series(n-1)

a = geometric_series(7)
print(a)