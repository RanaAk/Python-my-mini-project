####or we can return with direct valus

my_dict = { 'a': 1, 'b': 2, 'c': 3, 'd': 4 }

print(sum(my_dict.values()))
###we can do this in function

def sum_dict_values(my_dict):
    return sum(my_dict.values())


def main():
    sum_dict_values(my_dict)

if __name__ == "__main__":
    main()
