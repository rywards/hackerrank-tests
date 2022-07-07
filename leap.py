# function to determine if a year is a leap year
# leap year if the year is divisible by 4 unless it can be 
# divided by 100 then it is not UNLESS it is also evenly
# divisible by 400

def is_leap(year):
    leap = False
    
    if (year % 4 == 0):
        if (year % 100 == 0):
            if (year % 400 == 0):
                leap = True
            else:
                leap = False       
        if (year % 100 >=1):
            leap = True
    else:
        leap = False
    
    return leap

year = int(input())
print(is_leap(year))