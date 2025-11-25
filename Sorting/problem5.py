def bubble_sort(arr,k):
    n = len(arr)
    
    for i in range(n):
        swapped = False
        for j in range(0,n-i-1):
            if arr[j] % k > arr[j+1] % k:
                arr[j],arr[j+1] = arr[j+1],arr[j]
                swapped = True
                
        if not swapped:
            break
        
    return arr


print(bubble_sort([17, 3, 5, 12, 10, 9],4))