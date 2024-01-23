#we can print like that

my_dict = {("1'2", "4'5") : "ok", ("1'9", "4'8") : "not ok"}
#my_dict = {("19.07.53.2", "72.54'51.0"):"Mumbai", 
#             ("28.33'34.1", "77.06'16.6"):"Delhi"}
key = []

key_2 = []

f = []

for i in my_dict:
    key.append(i[0])
    key_2.append(i[1])


print(key)
print(key_2)   
print(f)



