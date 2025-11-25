def selection_sort(arr):
    n = len(arr)
    
    for father in range(n):
        min_index = father
        
        for son in range(father + 1,n):
            if arr[son] < arr[min_index]:
                min_index = son
                
        if father != min_index:
                arr[father],arr[min_index] = arr[min_index],arr[father]
        
    return arr


print(selection_sort([64,25,12,22,11]))


            
            