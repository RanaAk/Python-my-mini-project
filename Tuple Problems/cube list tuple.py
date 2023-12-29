
list1 = [1, 2, 5, 6]
#with out cube

res = [(x,x) for x in list1]


print(res)

###after Cube

result = [(x, pow(x,3)) for x in list1]
print("Cube of list is : ", result)

####or 

result = [(x, x**3) for x in list1]
print("Cube of list is(Another method) : ",result)

####################

