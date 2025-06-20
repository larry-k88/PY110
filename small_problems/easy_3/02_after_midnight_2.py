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

  - {Rewrite in own words}
     
  - Explicit requirements:
      - Rules
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
  - Input: 
  - Output:
    
  - Intermediate: 

High-level strategies:
  - 

Algorithm:  

  # Language agnostic for a non-programmer
  # Helper functions
  # Descriptive variable names
  # Run test cases through algo
  - 

'''
def after_midnight(time):
    pass

def before_midnight(time):
    pass

print(after_midnight("00:00") == 0)     # True
print(before_midnight("00:00") == 0)    # True
print(after_midnight("12:34") == 754)   # True
print(before_midnight("12:34") == 686)  # True
print(after_midnight("24:00") == 0)     # True
print(before_midnight("24:00") == 0)    # True