#Complete the function to return the previous and next number of a given numner.".
def previous_next(num):
  numbers = int(num)-1, int(num)+1
  return numbers


#Invoke the function with any interger at its argument. 
print(previous_next(179))