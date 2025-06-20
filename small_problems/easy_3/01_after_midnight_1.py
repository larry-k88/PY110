# The time of day can be represented as the number of minutes before or
# after midnight. If the number of minutes is positive, the time is
# after midnight. If the number of minutes is negative, the time is
# before midnight.

# Write a function that takes a time using this minute-based format and
# returns the time of day in 24-hour format (hh:mm). Your function
# should work with any integer input.

# You may not use Python's datetime module

'''
Problem:

    - Function takes a number and returns the time of day - number can
    be positive (after midnight) or negative (before midnight)

    - Input - integer
    - Output - string
     
    - Explicit requirements:
        - Arg is the number of minutes before or after midnight
    - Implicit requirements:
        - 0 --> midnight
        - number of days is irrelevant
    - Questions
        - 

Examples/Test Cases:
    - print(time_of_day(0) == "00:00")        # True
    - print(time_of_day(-3) == "23:57")       # True
    - print(time_of_day(35) == "00:35")       # True
    - print(time_of_day(-1437) == "00:03")    # True
    - print(time_of_day(3000) == "02:00")     # True
    - print(time_of_day(800) == "13:20")      # True
    - print(time_of_day(-4231) == "01:29")    # True

Data Structure:
    - % to get the number of minutes
    - f-string for the output  

Algorithm:  

    - Get the number of hours using %
    - Set starting points for hours and minutes

'''
'''# Initial problem
HOURS_PER_DAY = 24
MINUTES_PER_HOUR = 60

def time_of_day(num):
    hours = (num // MINUTES_PER_HOUR) % HOURS_PER_DAY
    minutes = num % MINUTES_PER_HOUR
    return(f'{hours:02d}:{minutes:02d}') # 'd' not needed but better

print(time_of_day(0) == "00:00")        # True
print(time_of_day(-3) == "23:57")       # True
print(time_of_day(35) == "00:35")       # True
print(time_of_day(-1437) == "00:03")    # True
print(time_of_day(3000) == "02:00")     # True
print(time_of_day(800) == "13:20")      # True
print(time_of_day(-4231) == "01:29")    # True
'''

# Consider normalising the argument to a value between 0 and 60 as this 
# clarifies that the % and // operators will work as expected (i.e. we 
# what what they'll do with positive numbers but may not be sure how 
# they work with negative ones, in this case, they are the same)

# Further Exploration
# How would you approach this problem if you could use Python's
# datetime class? Suppose you also needed to consider the day of the
# week? (Assume that delta_minutes is the number of minutes before or
# after midnight between Saturday and Sunday; in such a function, a
# delta_minutes value of -4231 would need to produce a return value of
# Thursday 01:29.)

import datetime as dt

def time_of_day(num):
    origin = dt.datetime(2025, 6, 15) # Ensure this is a Sunday at 00:00
    time_change = dt.timedelta(minutes=num)
    
    new_time = origin + time_change
    return new_time.strftime('%A %H:%M') 


print(time_of_day(-4231))

# print(time_of_day(0) == "00:00")        # True
# print(time_of_day(-3) == "23:57")       # True
# print(time_of_day(35) == "00:35")       # True
# print(time_of_day(-1437) == "00:03")    # True
# print(time_of_day(3000) == "02:00")     # True
# print(time_of_day(800) == "13:20")      # True
# print(time_of_day(-4231) == "01:29")    # True