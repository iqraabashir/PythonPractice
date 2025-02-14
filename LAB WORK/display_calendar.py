import calendar

year = int(input("Enter year (yyyy). "))
month = int(input("Enter month (1-12). "))
if month < 1 or month > 12:
    print("Invalid month.")
else:   
    print(calendar.month(year,month))