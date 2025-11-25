def power(a,b):
    if b==0:
        return 1
    
    half = power(a,b // 2)
    
    
    if  b % 2 == 0:
        return half * half
    
    else:
        return a * half * half
    
print(power(2,4))