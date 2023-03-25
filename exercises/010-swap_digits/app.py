#Complete the fuction to return the swapped digits of a given two-digit-interger.
def swap_digits(num):
  # Your code here
  dig1 = int(num)//10
  dig2 = int(num) % 10
  if (dig2 != 0):
    swap = dig2*10 + dig1
  else:
    swap = dig1
  return swap
   
#Invoke the function with any two digit interger as its argument
print(swap_digits(30))
