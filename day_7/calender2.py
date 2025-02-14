import calendar
from datetime import datetime

# Get the current date
today = datetime.now()
current_year = today.year
current_month = today.month
current_day = today.day

def display_calendar_with_highlight(year, month):
    cal = calendar.monthcalendar(year, month)
    print(calendar.month_name[month], year)
    print("Mo Tu We Th Fr Sa Su")
    for week in cal:
        for day in week:
            if day == current_day and month == current_month and year == current_year:
                # Highlight today's date (e.g., in red)
                print(f"\033[31m{day:2}\033[0m", end=" ")  # Red text
            elif day == 0:
                # Empty days (padding)
                print("  ", end=" ")
            else:
                print(f"{day:2}", end=" ")
        print()  # New line for the next week

# Example: Display calendar for current month and year
display_calendar_with_highlight(today.year, today.month)
