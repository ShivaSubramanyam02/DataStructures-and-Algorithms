def recursive(s):
    if s=="":
        return 0
    
    return 1 + recursive(s[1:])

print(recursive("subbu"))