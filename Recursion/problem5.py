def bubble_sort_recursive(arr, n=None, i=0):
    if n is None:
        n = len(arr)

    
    if n == 1:
        return

   
    if i == n - 1:
        bubble_sort_recursive(arr, n - 1, 0)
        return

    
    if arr[i] > arr[i + 1]:
        arr[i], arr[i + 1] = arr[i + 1], arr[i]

    
    bubble_sort_recursive(arr, n, i + 1)

arr = [3,5,0,9,8]
bubble_sort_recursive(arr)
print(arr)  
