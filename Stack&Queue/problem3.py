def remove_adjacent_duplicates(s):
    stack = []
    
    for char in s:
        if stack and stack[-1] == char:
            stack.pop()
            
        else:
            stack.append(char)
            
            
    result = stack
    
    print(result)
    return (result)


remove_adjacent_duplicates("abbaca") 
    