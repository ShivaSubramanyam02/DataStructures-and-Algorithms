s = "apple"

for father in range(0,len(s)):
    for son in range(father,len(s)):
        bag = ""
        for pickup in range(father,son+1):
            bag = bag + s[pickup]
            
        if bag[0] == "a" or bag[0] =="e"  or bag[0] =="i"  or bag[0] =="o"  or bag[0] =="u":
            print(bag,end=" ") 
                
           