######another type

def measure_bytes(obj):
    print(str(obj.__sizeof__()) + "bytes")
    print(obj.__sizeof__() , "bytes")

my_dict = { 'a': 1, 'b': 2, 'c': 3, 'd': 4 }
measure_bytes(my_dict)