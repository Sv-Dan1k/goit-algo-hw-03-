from datetime import datetime

def get_days_from_today(date):
    try:
        convert_date = datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        return "Incorrect date format. Please use the format 'YYYY-MM-DD'."
    
    today = datetime.today()
    difference = convert_date.date() - today.date()
    days_difference = difference.days
    return days_difference

print(get_days_from_today("2024-09-09"))
print(get_days_from_today("2023-09-09"))
print(get_days_from_today("2024.07.19"))
print(get_days_from_today("12-12-2000"))


