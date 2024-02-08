import itertools
str_ = "iamahero"

str_itr = iter(str_)

while True:
    try:
        print(next(str_itr))
    except StopIteration:
        quit()