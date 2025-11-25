s = "aeiouxyz"
count = 0

for father in range(0,len(s)):
    for son in range(father,len(s)):
        bag = ""
        for pickup in range(father,son+1):
            bag = bag + s[pickup]
            
        vowels = True
        for each_char in bag:
            if each_char   not in "aeiou":
                vowels = False
                break
            
        if vowels:
            count+=1
            
print(count)
            
     
            