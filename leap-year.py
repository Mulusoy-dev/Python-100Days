month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def is_leap(year):
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        str_leap="Leap year."
        month_days[1]=29
      else:
        str_leap="Not leap year."
    else:
      str_leap="Leap year."
      month_days[1]=29
  else:
    str_leap="Not leap year."



def days_in_month(year,month):
  is_leap(year) 
  print(month_days[month-1])
    
  
#🚨 Do NOT change any of the code below 
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)





