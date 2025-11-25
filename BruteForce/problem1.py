N = int(input("Enter how many Number : "))

K = int(input("Enter Target Number : "))

arr = list(map(int,input("Enter Numbers Sperated by Speces:").split()))

count  = 0


for i in range(N):
    for j in range(i+1,N): 
        if arr[i] + arr[j] == K:
            count += 1
        
        
        
print("Number of good pairs:", count)
