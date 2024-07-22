# `Day 38 - Intermediate+`

# `REVISION`: Working with Dates and Times in Python

This document provides an overview of handling dates and times in Python using the built-in `datetime` module. It covers
obtaining the current date and time, determining the day of the week, and formatting dates for display.

## Getting Started

To work with dates and times in Python, you primarily use the `datetime` module, which is part of Python's standard
library. No additional installation is required.

### Importing the Module

First, ensure you import the necessary components from the `datetime` module:

```
from datetime import datetime, timedelta 
from calendar import day_name
```

## Getting the Current Date and Time

To retrieve the current date and time, use the `datetime.now()` function:

```
current_datetime = datetime.now() 
print(current_datetime)
```

This will output the current date and time in the format `YYYY-MM-DD HH:MM:SS.ssssss`.

## Finding the Day of the Week

To find the day of the week for a given date, you can use the `weekday()` method of a `datetime` object. This method
returns an integer representing the day of the week, where Monday is 0 and Sunday is 6.

```
day_of_week = current_datetime.weekday() 
print(day_name[day_of_week])
```

This will print the name of the current day of the week.

## Formatting Dates

The `strftime()` method allows you to format `datetime` objects as strings in a variety of ways. Here are some common
formats:

- `%Y`: Year with century as a decimal number.
- `%m`: Month as a zero-padded decimal number.
- `%d`: Day of the month as a zero-padded decimal number.
- `%A`: Full weekday name.
- `%B`: Full month name.

Example:

```
python formatted_date = current_datetime.strftime("%A, %d %B %Y") 
print(formatted_date)
```

This will output the current date in the format `Weekday, DD Month YYYY`.

## Calculating Dates

The `timedelta` class represents a duration, the difference between two dates or times. You can use it to perform
arithmetic with dates:

### Today's Date

```
tomorrow = current_datetime + timedelta(days=1) 
print(tomorrow)
```

### Yesterday's Date

```
yesterday = current_datetime - timedelta(days=1) 
print(yesterday)
```

