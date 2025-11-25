#s = "shiva"

#for father in range(0,5):
    #for son in range(father,5):
        #bag = ""
        #for pickup in range(father,son+1):
            #bag = bag + s[pickup]
        #print(bag)
        
        
        
s = "abcab"

for father in range(0,len(s)):
    for son in range(father,len(s)):
        bag = ""
        for pickup in range(father,son+1):
            bag = bag + s[pickup]
            
        if bag[0] == "a":
            print(bag)
                
           
                
            
            
    
        
         

