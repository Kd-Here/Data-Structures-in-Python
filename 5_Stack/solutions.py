from stack import STACK


s = STACK()
def reverse_string(input):
    for i in input:
        s.push(i)

    str = " "
    while len(s.stack) > 0:
        str += s.peek()
        s.pop()
    print(str)


reverse_string("We had conquere COVID-19")