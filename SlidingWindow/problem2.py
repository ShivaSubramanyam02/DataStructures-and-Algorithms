def submaxarray(arr,n,k):
    if k>n:
        print("Invalid input")
        
    sum = 0
    for i in range(0,k):
        sum = sum + arr[i]
        
    max_sum = sum
    
    for i in range(1,n-k+1):
        sum = sum - arr[i-1] + arr[i+k-1]
        
        if sum > max_sum:
        
            max_sum = sum
        
    print("max sum is :",max_sum)


    
    
    
    
    

# n = 6
# arr = [2, 1, 5, 1, 3, 2]
# k = 3

submaxarray([2, 1, 5, 1, 3, 2],6,3)
