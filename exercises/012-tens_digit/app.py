#Complete the function to return the tens digit of a given interger
def tens_digit(num):
  centenas = int(num)%100
  decenas = centenas //10
  return decenas




#Invoke the function with any interger.
print(tens_digit(11459))