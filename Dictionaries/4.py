# # # my_dict = { 'b' : 18, 'a' :2, 'c' : 32, 'd' : 4}

# # # val = 'a'
# # # print(my_dict.get(val, "Not found"))

# # ######Another example
# # val = 'e'
# # if my_dict.get(val):
# #     print(my_dict[val])
# # else:
# #     print("Not found")

# ######Another example. Even we can set default value

# my_dict = { 'b' : 18, 'a' :2, 'c' : 32, 'd' : 4}

# key = 'e'

# my_dict.setdefault(key, 'Not found')

# print(my_dict[key])
####We can try and get

# my_dict = { 'b' : 18, 'a' :2, 'c' : 32, 'd' : 4}
# #my_dict = sorted(mydict.items(), key = lambda x: (x[1],x[0]))
# try:
#     print(my_dict)
#     print(list(my_dict))
#     print(list(my_dict.values()))
#     print(" ")
#     print(my_dict['e'])
# except KeyError:
#     print("Not found")

####Now in sort order

my_dict = { 'b' : 18, 'a' :2, 'c' : 32, 'd' : 4}
#my_dict = sorted(mydict.items(), key = lambda x: (x[1],x[0]))
try:
    print(my_dict)
    print(list(my_dict))
    my = list(my_dict.values())
    my.sort()
    print(my)
    sorted_dict = {i: my_dict[i] for i in my}
    print(sorted_dict)
    print(" ")
    print(my_dict['e'])
except KeyError:
    print("Not found")
