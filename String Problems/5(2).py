# #another type:


n="his is the lenght of the string"

s=n.split(" ") 
l=list(filter(lambda x: (len(x)%2==0),s)) 
print(l)

# #another type:

# python code to print even length words

n="This is the lenght of the string"
s=n.split(" ")
print([x for x in s if len(x)%2==0])