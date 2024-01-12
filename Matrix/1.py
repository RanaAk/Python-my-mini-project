

# test_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# print(str(test_list))
# print(test_list[0])

# update_list  = {test_list[0][i] :test_list[i+1] for i in range(len(test_list)-1) }


# print(update_list)

### Another type of solution

update = {}

for i in range(len(test_list)-1):
    update[test_list[0][i]] = test_list[i+1]

print(update)


# my_matrix = ()

