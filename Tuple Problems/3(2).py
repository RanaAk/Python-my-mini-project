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
