
# # import numpy as np
# # def matrix_add(A,B):

# #     A = np.array(A)
# #     B = np.array(B)

# #     return np.add(A,B)

# # def matrix_sub(A,B):

# #     A = np.array(A)
# #     B = np.array(B)

# #     return np.subtract(A,B)


# # print("This is matrix add"+ str(matrix_add([[1,2],[3,4]],[[1,2],[3,4]])))
# # print("This is matrix sub\n",matrix_sub([[1,2],[3,4]],[[1,2],[3,4]]))
# # ############but this method is not work for different length of matrix

###thats why we are goint to use zip function

def matrix_add(A,B):
    result = []
    for row_a,row_b in zip(A,B):
        result.append([sum(x) for x in zip(row_a,row_b)])
    return result

def matrix_sub(A,B):
    result = []
    for row_a,row_b in zip(A,B):
        result.append([x-y for x,y in zip(row_a,row_b)])
    return result

print("This is matrix add\n",matrix_add([[1,2],[3,4]],[[1,2],[3,4]]))
print("This is matrix sub\n",matrix_sub([[1,2],[3,4]],[[1,2],[3,4]]))

