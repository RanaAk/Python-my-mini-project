

s = "This is the lenght of the string"

def length(s):
    count = 0
    for i in s:
        count += 1
    return count

print(length(s))

# Another Type
def length(s):
    return len(s)

print(length(s))

# Another Type
def length(s):
    count = 0
    while s[count:]:
        count += 1
    return count

print(length(s))

# Another Type
