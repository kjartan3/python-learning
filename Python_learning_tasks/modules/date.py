# import datetime

from datetime import datetime  

today = datetime.now() 

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

print(today)
print(today.day)
print(today.month)

print(days[today.weekday()])  # prints the day of the week