##recursion : a function calls itself and it must have a base condition
# to avoid infinite loop 


def fact(n):
    if n==0 or n==1:
        return 1
    
    return n * fact(n-1)

print(fact(5))
    
    


    

