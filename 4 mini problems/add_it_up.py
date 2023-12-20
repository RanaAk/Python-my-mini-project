Number = int(input("Enter a number: "))

def add_it_up(Number):
  sum = 0
  for i in range(1,Number+1):
    sum = sum+i
  return sum


print(add_it_up(Number))