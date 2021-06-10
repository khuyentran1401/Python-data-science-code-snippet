from datetime import date, datetime, timedelta

beginning = '2020/01/03 23:59:00'
duration_in_minutes = 2500

# Find the beginning time
beginning = datetime.strptime(beginning, '%Y/%m/%d %H:%M:%S')

# Find duration in days
days = timedelta(minutes=duration_in_minutes)

# Find end time
end = beginning + days 
print(end)
# 2020-01-05 17:39:00