#Complete the funtion to compute how many seconds passed between the two timestamp.
def two_timestamp(hr1,min1,sec1,hr2,min2,sec2):
    sec_hr = hr2 - hr1
    sec_min = min2 - min1
    sec3 = sec2 - sec1
    seconds = (sec_hr*3600 + sec_min * 60 + sec3)
    return seconds


#Invoke the fuction and pass two timestamps(6 intergers) as its argument.
print(two_timestamp(1,1,1,2,2,2))