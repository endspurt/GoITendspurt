
from datetime import datetime

def get_days_from_today(date):
    # Convert the given date string to a datetime object
    given_date = datetime.strptime(date, '%Y-%m-%d').date()
    # Get today's date as a datetime object
    today_date = datetime.today().date()
    # Calculate the difference between the given date and today's date
    delta = today_date - given_date
    # Return the difference in days as an integer
    return delta.days

# Example function call
result = get_days_from_today("2024-04-09")
print(result)
