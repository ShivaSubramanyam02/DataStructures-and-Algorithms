n = int(input("Enter Number of digits"))  
arr1 = list(map(int, input(":").split()))
arr2 = list(map(int, input(":").split()))

for i in arr1:
    for j in arr2:
        if i == j:
            print(i)
            exit()  
