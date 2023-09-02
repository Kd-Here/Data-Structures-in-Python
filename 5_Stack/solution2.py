opposite = {
    '}': '{',
    ')' : '(',
    ']' : '['
}

from stack import STACK
s = STACK()
def is_balanced(input):
    if input[0] in '} ) ]':
            return False
    
    for i in range(len(input)):
        if input[i] in '( { [':
            s.push(input[i])
        elif input[i]  in '} ) ]': 
            if opposite[input[i]] == s.peek():
                s.pop()
            else:
                return False
            
    return True
            





if __name__ == '__main__':
    print(is_balanced("()[]{}"))
    print(is_balanced("{[()]}"))
    print(is_balanced("[(])"))
    print(is_balanced("[[{{(())}}]]"))
    print(is_balanced("{[()]({})}"))
    print(is_balanced("{{[(())]}}"))
    print(is_balanced("()()"))
    print(is_balanced("([)]"))
    print(is_balanced("[]"))
    print(is_balanced("{()}"))
    print(is_balanced("((()))"))
    print(is_balanced("{[()]}"))
    print(is_balanced("{[(])}"))
    print(is_balanced("()[]{}"))
