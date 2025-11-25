# def maxsubarray(arr,n,k):
#     max_sum = 0           # time complexity
#     for i in range(0,n-k+1): #------(n-k+1)
#         sum = 0
#         for j in range(i,i+k): # ------- k times 
#             sum = sum + arr[j]
#         if sum > max_sum:
#             max_sum = sum
    
#     print(max_sum)
        

# maxsubarray([1,4,2,10,23,3,1,0,20],9,4) this is brute force approach


def maxsubarray(arr,n,k):
    
    sum = 0
    for i in range(0,k):
        sum = sum + arr[i]
        
        
    
    max_sum = sum
    
    for i in range(1,n-k+1):
        sum = sum - arr[i-1] + arr[i+k-1]
        
        if sum > max_sum:
            max_sum = sum
            
    print("max sum is :",max_sum)
    
    
maxsubarray([1,4,2,10,23,3,1,0,20],9,4)
    
    


