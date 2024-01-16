
import numpy as np
def matrix_add(A,B):

    A = np.array(A)
    B = np.array(B)

    return np.add(A,B)

def matrix_sub(A,B):

    A = np.array(A)
    B = np.array(B)

    return np.subtract(A,B)


print("This is matrix add"+ str(matrix_add([[1,2],[3,4]],[[1,2],[3,4]])))
print("This is matrix sub\n",matrix_sub([[1,2],[3,4]],[[1,2],[3,4]]))
############but this method is not work for different length of matrix


