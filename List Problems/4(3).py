 def swapList(list, pos1, pos2):
    get = list[pos1], list[pos2]
      

    list[pos2], list[pos1] = get
      
    return list
a = [1,2,3,4,5,6,7]
print(swaplist(a,1,2))