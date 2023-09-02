def opposite(input,input2):
    if ord(input) == 40 and ord(input2) == 41:
        return True
    elif ord(input) == 91 and ord(input2) == 93:
        return True
    elif ord(input) == 123 and ord(input2) == 125:
        return True

from stack import STACK
s = STACK()
s1 = STACK()
k = []
def is_balanaced(input):
    if input[0] == '}' or input[0] == ']' or input[0] == ')':
        return False
    
    for i in range(len(input)):
        if input[i] == '(' or input[i] == '[' or input [i] == '{'or  input[i] == ')' or input[i] == ']' or input [i] == '}':
            k.append(input[i])

    for i in range(len(k)):
        if k[i] in ['(','[','{']:
            s.push(k[i])
        
        else:
            s1.push(k[i])
        
    print(s.stack,s1.stack)
    if len(s1.stack) == len(s.stack):
        for i in range(len(s1.stack)):
            if opposite(s.peek(),s1.stack[i]) == True:
                s.pop()
            elif opposite(s.stack[i],s1.stack[i]) ==  True:
                pass
            else:
                return False
        return True
    
    else: 
        return False





c = is_balanaced('[a+b]*(x+2y)*{gg+kk}')
print(c)
print(k)
print(s.stack)
print(s1.stack)