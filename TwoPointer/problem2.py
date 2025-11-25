#arr = [2, 2, 3, 3, 4, 4, 5]

#new_arr = []

#for i in range(len(arr)):
    #element = arr[i]
    #flag = False

    #for j in range(len(new_arr)):
        #if element == new_arr[j]:
            #flag = True
            #break

    #if flag == False:
        #new_arr.append(element)

#print(new_arr)


def remove_duplicates(arr):
    if not arr:
        return
    
    i = 0
    for j in range(1,len(arr)):
        if arr[j] != arr[i]:
            i+=1
            arr[i] = arr[j]
        
    unique_count = i+1
    
    for k in range(unique_count):
        print(arr[k])
        


remove_duplicates([1, 1, 2, 2, 3, 4, 4, 5])
















