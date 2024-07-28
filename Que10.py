
months = [
    ("January", 31), ("February", 28), ("March", 31), ("April", 30),
    ("May", 31), ("June", 30), ("July", 31), ("August", 31),
    ("September", 30), ("October", 31), ("November", 30), ("December", 31)
]

# Function to check if a year is a leap year
def leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

month_name = input("Enter the month name: ")
# year = None
 
if month_name.lower() == "february":
    year = int(input("Enter the year: "))


days_in_month = None
for month, days in months:
    if month.lower() == month_name.lower():
        if month.lower() == "february" and year is not None and leap_year(year):
            days += 1
        days_in_month = days
        break

if days_in_month is not None:
    print(f"Number of days in {month_name.capitalize()} : {days_in_month}")
else:
    print("Invalid month name entered.")
