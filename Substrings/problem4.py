s = "python"
result = []

for father in range(0,len(s)):
    for son in range(father,len(s)):
        bag = ""
        for pickup in range(father,son+1):
            bag = bag + s[pickup]
            
        if len(bag) == 2:
            result.append(bag)
            
            
print(result)