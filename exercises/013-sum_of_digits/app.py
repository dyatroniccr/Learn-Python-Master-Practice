#Complete the function "digits_sum" so that it prints the sum of a three digit number.
def digits_sum(num):
  centenas = int(num) // 100
  d_temp = int(num)%100
  decenas = d_temp //10
  unid = d_temp % 10
  sum = centenas + decenas + unid
  return sum


#Invoke the function with any three-digit-number
#You can try other three-digit numbers if you want
print(digits_sum(123))