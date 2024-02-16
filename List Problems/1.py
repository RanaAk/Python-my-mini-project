
a = [1,2,3,4,5,6,7,8,9,10]

b =[]

b = a[0]

a[0] = a[-1]

a[-1] = b

print(a)
new method
a = [1,2,3,4,5,6,7,8,9,10]
def swapList(newList):
    size = len(newList)

    temp = newList[0]
    newList[0] = newList[size-1]
    newList[size-1] = temp

    return newList

print(swapList(a))


def swapList(list):
    list[0], list[-1] = list[-1], list[0]
    return list

a = [1,2,3,4,5,6,7,8,9,10]
print(swapList(a))

#############################################################################################################


