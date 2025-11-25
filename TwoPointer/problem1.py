def two_pointer_pair_sum(arr,k):
    arr.sort()
    left = 0 
    right = len(arr) - 1
    
    
    while left < right:
        sum = arr[left] + arr[right]
        
        
        if sum == k:
            return True
        
        elif sum < k:
            left +=1
        else:
            right -=1
            
            
arr = [7,4,9,6,21,8,11,17]

k = 30

print(two_pointer_pair_sum(arr,k))             