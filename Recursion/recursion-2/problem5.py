def remove_adjacent_duplicates(s):
    if len(s) <= 1:
        return s

    i = 0
    result = ""
    changed = False

    while i < len(s):
        if i < len(s) - 1 and s[i] == s[i + 1]:
            changed = True
            while i < len(s) - 1 and s[i] == s[i + 1]:
                i += 1
            i += 1
        else:
            result += s[i]
            i += 1

    if not changed:
        return result

    return remove_adjacent_duplicates(result)

s = input().strip()
final = remove_adjacent_duplicates(s)
if final == "":
    print("empty string")
else:
    print(final)
