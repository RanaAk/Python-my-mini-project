
a = "imiimi"

def check_palindrome_and_symmetric(a):
    l = int(len(a)/2)
    first_half = a[:l]
    second_half = a[l:]

    if first_half == second_half:
        print("symmetric") 
    else:
        print("not symmetric")
    
    if first_half == second_half[::-1]:
        print("palindrome")
    else:
        print("not palindrome")

check_palindrome_and_symmetric(a)




