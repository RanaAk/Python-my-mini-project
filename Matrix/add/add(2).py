###thats why we are goint to use zip function

def matrix_add(A,B):
    result = []
    for row_a,row_b in zip(A,B):
        result.append([sum(x) for x in zip(row_a,row_b)])
    return result

