# As seen in the previous exercise, the time of day can be represented
# as the number of minutes before or after midnight. If the number of
# minutes is positive, the time is after midnight. If the number of
# minutes is negative, the time is before midnight.

# Write two functions that each take a time of day in 24 hour format,
# and return the number of minutes before and after midnight,
# respectively. Both functions should return a value in the range 0
# through 1439.

# You may not use Python's datetime module.
# Disregard Daylight Savings and Standard Time and other irregularities.

'''
Problem:

  - 2 functions, one returns the number of minutes before midnight and 
  the other that returns the number of minutes after midnight
     
  - Explicit requirements:
      - converts time to minutes
      - no datetime module
      - output within range 0-1439 mins
  - Implicit requirements:
      - 
  - Questions
      - 

Examples/Test Cases:
    - print(after_midnight("00:00") == 0)     # True
    - print(before_midnight("00:00") == 0)    # True
    - print(after_midnight("12:34") == 754)   # True
    - print(before_midnight("12:34") == 686)  # True
    - print(after_midnight("24:00") == 0)     # True
    - print(before_midnight("24:00") == 0)    # True

Data Structure:
  - Input: string (time in 24 hour format)
  - Output: Integer (between 0 and 1439)
    
  - Intermediate: string to list, then save values as integers 

High-level strategies:
- Split the string and extract/save the int values of hours and mins
- Calculate the number of hours after midnight
- Use the fact that the number of hours before midnight would be:
    mins in a day - mins before midnight

Algorithm:  

  # Language agnostic for a non-programmer
  # Helper functions
  # Descriptive variable names
  # Run test cases through algo
- Helper function (after_midnight):
    - Turn the string into a list using split and then save the numbers
    either side of `:` as variables `hours` and `minutes`
    - Calculate and return the total number of minutes
- before_midnight: take the return value of the helper function and find
the difference between the number of minutes in a day and that value

'''

HOURS_PER_DAY = 24
MINS_PER_HOUR = 60
MINS_PER_DAY = HOURS_PER_DAY * MINS_PER_HOUR

def after_midnight(time):
    hours = int(time.split(':')[0])
    mins = int(time.split(':')[1])
    total_mins = ((hours * MINS_PER_HOUR) + mins) % MINS_PER_DAY
    return total_mins

def before_midnight(time):
    delta_mins = (MINS_PER_HOUR * HOURS_PER_DAY) - after_midnight(time)
    if delta_mins == MINS_PER_DAY:
        return 0
    return delta_mins

print(after_midnight("00:00") == 0)     # True
print(before_midnight("00:00") == 0)    # True
print(after_midnight("12:34") == 754)   # True
print(before_midnight("12:34") == 686)  # True
print(after_midnight("24:00") == 0)     # True
print(before_midnight("24:00") == 0)    # True

# Further exploration: How would these functions change if you could use
# the Python's datetime.datetime class? 

from datetime import datetime

HOURS_PER_DAY = 24
MINS_PER_HOUR = 60
MINS_PER_DAY = HOURS_PER_DAY * MINS_PER_HOUR

def after_midnight(time):
    new_time = "00:00" if time == "24:00" else time
    time_obj = datetime.strptime(new_time, '%H:%M')
    return (time_obj.hour * MINS_PER_HOUR) + time_obj.minute

def before_midnight(time):
    return (MINS_PER_DAY - after_midnight(time)) % MINS_PER_DAY


print(after_midnight("00:00") == 0)     # True
print(before_midnight("00:00") == 0)    # True
print(after_midnight("12:34") == 754)   # True
print(before_midnight("12:34") == 686)  # True
print(after_midnight("24:00") == 0)     # True
print(before_midnight("24:00") == 0)    # True