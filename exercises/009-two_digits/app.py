#Complete the function to return the tens digit and the ones digit of any interger.
def two_digits(digit):
  dig1 = int(digit)//10
  dig2 = int(digit) % 10
  return dig1,dig2
   


#Invoke the function with any interger as its argument.
print(two_digits(79))
