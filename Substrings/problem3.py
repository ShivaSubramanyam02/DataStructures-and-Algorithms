s = "abcab"

for father in range(0,len(s)):
    for son in range(father,len(s)):
        bag = ""
        for pickup in range(father,son+1):
            bag = bag + s[pickup]
            
        if bag[0] == bag[-1]:
            print(bag)
                
           