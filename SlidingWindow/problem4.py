def length_of_longest_substring(s):
    char_index = {}
    max_length = 0
    start = 0  

    for end in range(len(s)):
        if s[end] in char_index and char_index[s[end]] >= start:
            start = char_index[s[end]] + 1  

        char_index[s[end]] = end  
        max_length = max(max_length, end - start + 1)

    return max_length



def longest_unique_substring(s):
    seen = set()
    left = 0
    max_len = 0

    for right in range(len(s)):
        while s[right] in seen:
            seen.remove(s[left])
            left += 1

        seen.add(s[right])
        max_len = max(max_len, right - left + 1)

    return max_len 

