# RECURSIVE means STACK
def recursive_sum(n):
    print("i",n)


    if n > 1:
        c = recursive_sum(n-1)
        print(c,"returned")

    if n == 1:
        print("-------------------------------")
    
    print("j",n)
    return n
    
    



if __name__ == "__main__":
    recursive_sum(5)