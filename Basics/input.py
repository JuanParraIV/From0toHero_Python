def days_to_hours(days): 
  return f"{days} days are {days * 24} hours"

days = input('Enter Number of days\n')
days_int=int(days)
value = days_to_hours(days_int)
print(value)