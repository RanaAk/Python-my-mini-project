######with np function

import numpy as np
my_dict = { 'a': 1, 'b': 2, 'c': 3, 'd': 4 }

def sum_dict_values(my_dict):
    my_list = list(my_dict.values())
    my_array = np.array(my_list)
    my_sum = np.sum(my_array)
    return my_sum


print(sum_dict_values(my_dict))
