Number = input("Enter a number: ")

# try:
#   Number = int(Number)
# except ValueError:
#   print("You entered a string!. Please entered Integer only")
#   quit()
  
#method one
def sum_digits(Number):
    return sum(int(digit) for digit in Number)


#method Two
def add_it(Number):
  add = 0
  for digit in Number:
    add = add + int(digit)
  return add
    


a = add_it(Number)
print(a)