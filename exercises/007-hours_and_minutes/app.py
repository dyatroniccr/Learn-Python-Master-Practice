#Complete the function to calculate how many hours and minutes are passed since midnight.
def hours_minutes(secs):  
  minutes = int(secs) // 60
  min_pass = minutes % 60
  hours = minutes // 60
  return hours, min_pass

#Invoke the funtion and pass any interger as its argument.
print(hours_minutes(3900))