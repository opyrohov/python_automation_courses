"""
Lecture 11: Working with Datetime Module
This file demonstrates how to work with dates and times in Python.
"""

from datetime import datetime, date, time, timedelta
import time as time_module

# ============================================
# CURRENT DATE AND TIME
# ============================================
print("=" * 60)
print("CURRENT DATE AND TIME")
print("=" * 60)

# Get current datetime
now = datetime.now()
print(f"Current datetime: {now}")
print(f"Type: {type(now)}")

# Get current date only
today = date.today()
print(f"\nCurrent date: {today}")
print(f"Type: {type(today)}")

# Create specific time
specific_time = time(14, 30, 45)  # 2:30:45 PM
print(f"\nSpecific time: {specific_time}")
print(f"Type: {type(specific_time)}")
print()

# ============================================
# DATETIME COMPONENTS
# ============================================
print("=" * 60)
print("DATETIME COMPONENTS")
print("=" * 60)

now = datetime.now()
print(f"Full datetime: {now}")
print(f"Year: {now.year}")
print(f"Month: {now.month}")
print(f"Day: {now.day}")
print(f"Hour: {now.hour}")
print(f"Minute: {now.minute}")
print(f"Second: {now.second}")
print(f"Microsecond: {now.microsecond}")
print(f"Day of week: {now.weekday()} (0=Monday, 6=Sunday)")
print(f"ISO day of week: {now.isoweekday()} (1=Monday, 7=Sunday)")
print()

# ============================================
# CREATING SPECIFIC DATES
# ============================================
print("=" * 60)
print("CREATING SPECIFIC DATES")
print("=" * 60)

# Create specific date
birthday = date(1990, 5, 15)
print(f"Birthday: {birthday}")

# Create specific datetime
meeting = datetime(2024, 12, 25, 14, 30, 0)
print(f"Meeting: {meeting}")

# Create from timestamp
timestamp = 1735142400
from_timestamp = datetime.fromtimestamp(timestamp)
print(f"From timestamp: {from_timestamp}")
print()

# ============================================
# FORMATTING DATES - strftime
# ============================================
print("=" * 60)
print("FORMATTING DATES - strftime()")
print("=" * 60)

now = datetime.now()

# Common format codes
print(f"ISO format: {now.strftime('%Y-%m-%d %H:%M:%S')}")
print(f"US format: {now.strftime('%m/%d/%Y')}")
print(f"European format: {now.strftime('%d/%m/%Y')}")
print(f"Full month name: {now.strftime('%B %d, %Y')}")
print(f"Abbreviated month: {now.strftime('%b %d, %Y')}")
print(f"Day name: {now.strftime('%A')}")
print(f"Abbreviated day: {now.strftime('%a')}")
print(f"12-hour time: {now.strftime('%I:%M %p')}")
print(f"24-hour time: {now.strftime('%H:%M:%S')}")
print(f"Custom format: {now.strftime('%A, %B %d, %Y at %I:%M %p')}")
print()

# ============================================
# PARSING DATES - strptime
# ============================================
print("=" * 60)
print("PARSING DATES - strptime()")
print("=" * 60)

# Parse date strings into datetime objects
date_string1 = "2024-12-25"
parsed1 = datetime.strptime(date_string1, "%Y-%m-%d")
print(f"Parsed '{date_string1}': {parsed1}")

date_string2 = "12/25/2024 14:30"
parsed2 = datetime.strptime(date_string2, "%m/%d/%Y %H:%M")
print(f"Parsed '{date_string2}': {parsed2}")

date_string3 = "December 25, 2024"
parsed3 = datetime.strptime(date_string3, "%B %d, %Y")
print(f"Parsed '{date_string3}': {parsed3}")
print()

# ============================================
# TIMEDELTA - DATE ARITHMETIC
# ============================================
print("=" * 60)
print("TIMEDELTA - DATE ARITHMETIC")
print("=" * 60)

now = datetime.now()
print(f"Now: {now}")

# Add days
tomorrow = now + timedelta(days=1)
print(f"Tomorrow: {tomorrow}")

next_week = now + timedelta(weeks=1)
print(f"Next week: {next_week}")

# Subtract days
yesterday = now - timedelta(days=1)
print(f"Yesterday: {yesterday}")

# Combine different units
future = now + timedelta(days=7, hours=3, minutes=30)
print(f"7 days, 3 hours, 30 minutes from now: {future}")

# Calculate difference between dates
difference = future - now
print(f"\nTime difference: {difference}")
print(f"Total seconds: {difference.total_seconds()}")
print(f"Days: {difference.days}")
print()

# ============================================
# COMPARING DATES
# ============================================
print("=" * 60)
print("COMPARING DATES")
print("=" * 60)

date1 = datetime(2024, 12, 25)
date2 = datetime(2025, 1, 1)

print(f"Date 1: {date1}")
print(f"Date 2: {date2}")
print(f"date1 < date2: {date1 < date2}")
print(f"date1 > date2: {date1 > date2}")
print(f"date1 == date2: {date1 == date2}")
print()

# Check if date is in the past or future
now = datetime.now()
past_date = datetime(2020, 1, 1)
future_date = datetime(2030, 1, 1)

print(f"Is {past_date.date()} in the past? {past_date < now}")
print(f"Is {future_date.date()} in the future? {future_date > now}")
print()

# ============================================
# PRACTICAL EXAMPLES
# ============================================
print("=" * 60)
print("PRACTICAL EXAMPLES")
print("=" * 60)

# Example 1: Calculate age
def calculate_age(birth_date):
    """Calculate age from birth date"""
    today = date.today()
    age = today.year - birth_date.year
    # Adjust if birthday hasn't occurred this year
    if (today.month, today.day) < (birth_date.month, birth_date.day):
        age -= 1
    return age

birthday = date(1990, 5, 15)
age = calculate_age(birthday)
print(f"Birth date: {birthday}")
print(f"Age: {age} years old")
print()

# Example 2: Days until event
def days_until(target_date):
    """Calculate days until a target date"""
    today = date.today()
    delta = target_date - today
    return delta.days

new_year = date(2025, 1, 1)
days_left = days_until(new_year)
print(f"Days until New Year 2025: {days_left}")
print()

# Example 3: Is weekend?
def is_weekend(check_date):
    """Check if a date is a weekend"""
    return check_date.weekday() in [5, 6]  # Saturday=5, Sunday=6

today = date.today()
print(f"Is today ({today.strftime('%A')}) a weekend? {is_weekend(today)}")
print()

# Example 4: Get date range
def get_date_range(start_date, end_date):
    """Generate list of dates between start and end"""
    dates = []
    current = start_date
    while current <= end_date:
        dates.append(current)
        current += timedelta(days=1)
    return dates

start = date(2024, 12, 25)
end = date(2024, 12, 31)
date_range = get_date_range(start, end)
print("Dates from Dec 25 to Dec 31, 2024:")
for d in date_range:
    print(f"  {d.strftime('%A, %B %d')}")
print()

# Example 5: Format for different regions
def format_for_region(dt, region):
    """Format datetime for different regions"""
    formats = {
        "US": "%m/%d/%Y %I:%M %p",
        "EU": "%d/%m/%Y %H:%M",
        "ISO": "%Y-%m-%d %H:%M:%S",
        "READABLE": "%A, %B %d, %Y at %I:%M %p"
    }
    return dt.strftime(formats.get(region, formats["ISO"]))

now = datetime.now()
print("Current time in different formats:")
print(f"  US: {format_for_region(now, 'US')}")
print(f"  European: {format_for_region(now, 'EU')}")
print(f"  ISO: {format_for_region(now, 'ISO')}")
print(f"  Readable: {format_for_region(now, 'READABLE')}")
print()

# ============================================
# TIMING CODE EXECUTION
# ============================================
print("=" * 60)
print("TIMING CODE EXECUTION")
print("=" * 60)

# Using datetime
start = datetime.now()
time_module.sleep(0.5)  # Simulate some work
end = datetime.now()
duration = end - start
print(f"Execution time (datetime): {duration}")
print(f"Seconds: {duration.total_seconds()}")
print()

# ============================================
# WORKING WITH TIMESTAMPS
# ============================================
print("=" * 60)
print("WORKING WITH TIMESTAMPS")
print("=" * 60)

now = datetime.now()
timestamp = now.timestamp()
print(f"Datetime: {now}")
print(f"Unix timestamp: {timestamp}")

# Convert timestamp back to datetime
from_ts = datetime.fromtimestamp(timestamp)
print(f"From timestamp: {from_ts}")
print()

# ============================================
# COMMON FORMAT CODES REFERENCE
# ============================================
print("=" * 60)
print("COMMON FORMAT CODES REFERENCE")
print("=" * 60)
print("""
Date Formatting Codes (strftime):
  %Y - Year with century (2024)
  %y - Year without century (24)
  %m - Month as number (01-12)
  %B - Full month name (January)
  %b - Abbreviated month (Jan)
  %d - Day of month (01-31)
  %A - Full weekday name (Monday)
  %a - Abbreviated weekday (Mon)
  %H - Hour 24-hour (00-23)
  %I - Hour 12-hour (01-12)
  %M - Minute (00-59)
  %S - Second (00-59)
  %p - AM/PM
  %w - Weekday as number (0-6, 0=Sunday)
  %j - Day of year (001-366)
  %U - Week number of year (00-53, Sunday as first day)
  %W - Week number of year (00-53, Monday as first day)

Common Patterns:
  ISO 8601: %Y-%m-%d %H:%M:%S
  US Date: %m/%d/%Y
  European Date: %d/%m/%Y
  Readable: %B %d, %Y at %I:%M %p
""")
