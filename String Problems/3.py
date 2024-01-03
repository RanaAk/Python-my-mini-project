#Remove Ith character from string

def remove(string, i):
    s = string.replace(string[i], "")
    return s

print(remove("this is a test", 2))

###
######str = 'Geeks123For123Geeks'
  
######print(str.translate({ord(i): None for i in '123'}))


