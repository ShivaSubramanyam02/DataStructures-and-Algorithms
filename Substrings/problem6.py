s = "abc"
count = 0

for father in range(0,len(s)):
    for son in range(father,len(s)):
        bag = ""
        for pickup in range(father,son+1):
            bag = bag + s[pickup]
            
        if "a" in  bag:
            count+=1 
            
            
print(count)
                