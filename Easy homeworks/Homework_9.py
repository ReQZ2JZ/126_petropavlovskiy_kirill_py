def words(s):
    result = ""
    upper = False
    for c in s:
        if c.isalpha():
            if upper:
                result += c.upper()
                upper = False
            else:
                result += c.lower()
                upper = True
        else:
            result += c
    return result
s = "Coconut"
result = words(s)
print(result)