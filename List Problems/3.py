def swapList(list):
    get = list[-1], list[0] 
    list[0], list[-1] = get
    return list


a = [1,2,3,4,5,6,7,8,9,10]
print(swapList(a))
