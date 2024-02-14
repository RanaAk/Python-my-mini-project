my_set = set([12, 10, 13, 15, 8, 9])
 
for i in range(len(my_set)):
    my_set.remove(next(iter(my_set)))
    print(my_set)

my_set = set([12, 10, 13, 15, 8, 9])

while my_set:
    my_set.discard(max(my_set))
    print(my_set)