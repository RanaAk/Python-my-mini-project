

my_list = [1,2,1,4,5,1,5,6,6,7,8]

List = []

for i in my_list:
    found = False
    for j in range(len(List)):
        if i in List[j]:
            List[j].append(i)
            found = True
            break
    if not found:
        List.append([i])
    
print(str(List))

