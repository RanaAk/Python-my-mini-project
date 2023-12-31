# def sumALl(tup):
# 	temp = list(tup)
# 	count = 0
# 	for i in temp:
# 		count += i
# 	return count

# tup = (5, 20, 3, 7, 6, 8)
# print(sumAll(tup))
#This method doesn't work on tup = ([1,2], [3,4], [5,6])
#SO here is another method

tup = ([1,2], [3,4], [5,6])
print("The tuple ;" + str(tup))

res = sum(list(map(sum, list(tup))))

print("The summation of tuple elements are : " + str(res))

######With math function librabry
import math
tup = ([1,2], [3,4], [5,6])
print("The tuple ;" + str(tup))


result = math.fsum(list(map(sum, list(tup))))
print(result)
# ###############but if the tup i lik #tup = (1,2,3,4,5,6)

tup = (1,2,3,4,5,6)

result = math.fsum(tup)
print(result)
