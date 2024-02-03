####another beautiful function example
my_dict = { 'a': 1, 'b': 2, 'c': 3, 'd': 4 }
def sum_dict_values(my_dict):
    return sum(my_dict[key] for key in my_dict)

def main():
    a = sum_dict_values(my_dict)
    print(a)

if __name__ == "__main__":
    main()