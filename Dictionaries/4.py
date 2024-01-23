my_dict = { 'b' : 18, 'a' :2, 'c' : 32, 'd' : 4}

val = 'a'
print(my_dict.get(val, "Not found"))

######Another example
val = 'e'
if my_dict.get(val):
    print(my_dict[val])
else:
    print("Not found")



