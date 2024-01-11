######Another type of solution

my_list = [1,2,1,4,5,1,5,6,6,7,8]

group = {}

for i in my_list:
    if i in group:
        group[i].append(i)
    else:
        group[i] = [i]

print(list(group.values()))