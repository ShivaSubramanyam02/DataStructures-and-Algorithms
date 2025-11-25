def subarray_with_given_sum(arr,n,target):
    start = 0
    current_sum = 0
    
    for end in range(n):
        current_sum += arr[end]
        
        while current_sum > target and start <= end:
            current_sum -= arr[start]
            start+=1
            
            
        if current_sum == target:
            return "YES"
        
    return "NO"


print(subarray_with_given_sum([1, 4, 20, 3, 10, 5],6, 33))
        