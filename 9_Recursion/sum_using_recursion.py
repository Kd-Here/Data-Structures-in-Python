# Recursion functions works in stack manner
def recursive_sum(n):
    if n == 1:
        return 1
    
    else:
        return n + recursive_sum(n-1)
                  #The recursive happens here when it's n=1 it's starts pop of stack 



if __name__ == "__main__":
    
    s = recursive_sum(5)
    print(s)


"""To see how this work check this visualization website"""
# https://pythontutor.com/render.html#code=def%20recursive_sum%28n%29%3A%0A%20%20%20%20if%20n%20%3D%3D%201%3A%0A%20%20%20%20%20%20%20%20return%201%0A%20%20%20%20else%3A%0A%20%20%20%20%20%20%20%20return%20n%20%2B%20recursive_sum%28n-1%29%0A%0A%0A%0A%0Aif%20__name__%20%3D%3D%20%22__main__%22%3A%0A%20%20%20%20%0A%20%20%20%20s%20%3D%20recursive_sum%285%29%0A%20%20%20%20print%28s%29&cumulative=false&curInstr=23&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false