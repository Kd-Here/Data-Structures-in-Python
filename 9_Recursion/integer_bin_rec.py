"""Python program to convert an integer to a string in any base"""

def int_to_string(number,base):
    if number == 0:
        return ""
    a = number%2
    return   int_to_string(number//base,base) + str(a) 

print(int_to_string(2835,2))


