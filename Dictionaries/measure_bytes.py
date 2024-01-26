import sys

# Measure bytes of an object
def measure_bytes(obj):
    print(str(sys.getsizeof(obj)) +  "bytes")


my_dict = { 'a': 1, 'b': 2, 'c': 3, 'd': 4 }
measure_bytes(my_dict)


