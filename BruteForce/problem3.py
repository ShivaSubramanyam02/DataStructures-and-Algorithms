num = int(input("Enter a number: "))

if num <= 1:
    print("NO")
    
else:
    is_prime = True
    for i in range(2,num):
        if num%i==0:
            is_prime = False
            
    if is_prime:
        print("Yes")
    else:
        print('NO') 

            
#2 code 

num = int(input("--"))
count = 0

for i in range(1,num+1):
    if num % i == 0:
        count+=1
        
if count==2:
    print("prime")
else:
    print("Not a prime")