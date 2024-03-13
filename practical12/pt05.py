import calendar

def display_calendar(year, month):
    cal = calendar.month(year, month)
    print("Calendar for {}/{}:".format(year, month))
    print(cal)

# Example usage:
year = 2024
month = 3
display_calendar(year, month)
