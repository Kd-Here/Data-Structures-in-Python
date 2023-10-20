"""
The Greatest Common Divisor (GCD), also known as the Greatest Common Factor (GCF) or Highest Common Factor (HCF), of two or more numbers is the largest positive integer that divides each of the numbers without leaving a remainder.

For example, let's find the GCD of 12 and 18:

List the divisors of each number:

Divisors of 12: 1, 2, 3, 4, 6, 12
Divisors of 18: 1, 2, 3, 6, 9, 18
Find the divisors that both numbers have in common:

Common divisors: 1, 2, 3, 6
Identify the largest common divisor, which is 6.

So, the GCD of 12 and 18 is 6.

"""
# approach: 
# 1) factors of both
# 2) Intersection in them
# 3) max of them



# def factors(a):
#     s = []
#     for i in range(1,a):
#         if a%i == 0:
#             s.append(i)
#     return s

# def finding_factors(a,i=1,factors=[]):
#     if a == i:
#         return factors
#     elif a % i == 0:
#         factors.append(i)
#     return finding_factors(a,i+1,factors)
    
# l = finding_factors(9)
# print(l)


def greatest_common_factor(a,b):
     

    def finding_factors(a,i=1,factors=None):
        if factors is None:
            factors = []
        if a == i:
            return factors
        elif a % i == 0:
             factors.append(i)
        return finding_factors(a,i+1,factors)
        
    factors_of_a = finding_factors(a)
    factors_of_b = finding_factors(b)
    
    common_factor  = set(factors_of_a) & set(factors_of_b)
    print(max(common_factor))


greatest_common_factor(12,18)

def Recurgcd(a, b):
	low = min(a, b)
	high = max(a, b)

	if low == 0:
		return high
	elif low == 1:
		return 1
	else:
		return Recurgcd(low, high%low)
print(Recurgcd(12,14))
