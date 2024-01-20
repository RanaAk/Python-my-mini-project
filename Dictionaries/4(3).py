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
