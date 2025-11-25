def max_water_container(heights: list) -> None:
    left = 0 
    right = len(heights)-1
    
    max_area = 0
    
    
    while left < right:
        height = min(heights[left],heights[right])
        width = right - left
        area = height * width
        
        max_area = max(max_area,area)
        
        
        
        if heights[left] < heights[right]:
            left+=1
            
        else:
            right -= 1
            
    print(max_area)
    
max_water_container([1, 8, 6, 2, 5, 4, 8, 3, 7])
