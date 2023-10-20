# First approach
def sumofnumbers_type1(n):
    if len(n) == 0:
        return 0
    k = int(n[-1])
    return k + sumofnumbers_type1(n[:-1])


# a = sumofnumbers_type1(str(354))
# print(a)



"""
234 // 10 is an integer division operation. It calculates how many times 10 can be evenly divided into 234 without any remainder. The result of 234 // 10 is 23 because 10 goes into 234 a total of 23 times without any remainder. So, it represents the quotient of the division.

234 % 10 is a modulo operation. It calculates the remainder when you divide 234 by 10. The result of 234 % 10 is 4 because when you divide 234 by 10, you get 23 with a remainder of 4. So, it represents the remainder of the division.

Here's a breakdown of the two operations:

234 // 10:

Divide 234 by 10: 234 / 10 = 23.4
The // operator discards the decimal part, giving you the integer result, which is 23.4 after decimal part everything is discarded
234 % 10:

Divide 234 by 10: 234 / 10 = 23.4
The % operator gives you the remainder, which is 4 in this case.

def sumofnumbers_type2(n):

    a = n // 2 
    print(a)
    a = n % 10
    print(a)

at last iteration in recursion
 "2 // 10" performs integer division of 2 by 10.

When you divide 2 by 10, the result is 0 with no remainder. 
The // operator in Python is used for integer division, which discards the decimal part, so the result of "2 // 10" is 0. something ignore it

In this case, it indicates that 10 cannot be evenly divided into 2, and there's no whole number quotient.

"""
#Second approach
def sumofnumbers_type2(n):
    if n == 0:
        return 0
    return (n % 10) + sumofnumbers_type2(n//10)

c = sumofnumbers_type2(2345)
print(c)