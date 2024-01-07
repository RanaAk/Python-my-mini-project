
# def find_a_b(str_):
#     j =0;
#     sp = str_.split()
#     for i in range(len(sp)):
#         if a and b in sp[i]:
#             j+=1
#     return j

# print(find_a_b(str_))

def find_a_b(str_, a , b):
    count = 0
    if a in str_ and b in str_:
        a_count = str_.count(a)
        b_count = str_.count(b)
    if a_count == b_count:
        count = a_count
    return count

def main():
    str_ = "i have a cat and a hat and a cat  and a  "
    a = 'cat'
    b = 'hat'
    i = find_a_b(str_, a, b)
    if(i>0):
        print("True")
        print(f"cat and hat both are present {i} number of times.")
    else:
        print("False")
        print(f"cat and hat both are present {i} number of times.")

if __name__ == "__main__":
    main()