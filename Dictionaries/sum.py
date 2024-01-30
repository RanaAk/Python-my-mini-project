# # # # my_dict = { 'a': 1, 'b': 2, 'c': 3, 'd': 4 }

# # # # j=0;
# # # # for i in my_dict:
# # # #     j+=my_dict[i]
# # # #     print(j)

# # # my_dict = { 'a': 1, 'b': 2, 'c': 3, 'd': 4 }

# # # my_list = list(my_dict.values())


# # # print(sum(my_list))

# # # #####or 
# # # my_list = []
# # # for i in my_dict:
# # #     my_list.append(my_dict[i])

# # # print(sum(my_list))

# # ####or we can return with direct valus

# # my_dict = { 'a': 1, 'b': 2, 'c': 3, 'd': 4 }

# # print(sum(my_dict.values()))
# # ###we can do this in function

# # def sum_dict_values(my_dict):
# #     return sum(my_dict.values())


# # def main():
# #     sum_dict_values(my_dict)

# # if __name__ == "__main__":
# #     main()

# ####another beautiful function example
# my_dict = { 'a': 1, 'b': 2, 'c': 3, 'd': 4 }
# def sum_dict_values(my_dict):
#     return sum(my_dict[key] for key in my_dict)

# def main():
#     a = sum_dict_values(my_dict)
#     print(a)

# if __name__ == "__main__":
#     main()

######with np function

import numpy as np
my_dict = { 'a': 1, 'b': 2, 'c': 3, 'd': 4 }

def sum_dict_values(my_dict):
    my_list = list(my_dict.values())
    my_array = np.array(my_list)
    my_sum = np.sum(my_array)
    return my_sum


print(sum_dict_values(my_dict))

