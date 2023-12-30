import numpy as np

test_tup = (1, 2, 3, 4, 5, 6)

 
#tup to np array
test_array = np.array(test_tup)
 

print("The original tuple is : " + str(test_tup))
 

res = np.sum(test_array)
 

print("The summation of tuple elements are : " + str(res))

####the fun part is np works on both
tup = ([1,2], [3,4], [5,6])

test = np.array(tup)

result = np.sum(test)
print("original tuple is : " + str(tup))

print(result)