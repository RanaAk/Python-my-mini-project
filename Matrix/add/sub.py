def matrix_sub(A,B):
    result = []
    for row_a,row_b in zip(A,B):
        result.append([x-y for x,y in zip(row_a,row_b)])
    return result

print("This is matrix add\n",matrix_add([[1,2],[3,4]],[[1,2],[3,4]]))
print("This is matrix sub\n",matrix_sub([[1,2],[3,4]],[[1,2],[3,4]]))
