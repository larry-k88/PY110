# Some people believe that Fridays that fall on the 13th day of the
# month are unlucky days. Write a function that takes a year as an
# argument and returns the number of Friday the 13ths in that year. You
# may assume that the year is greater than 1752, which is when the
# United Kingdom adopted the modern Gregorian Calendar. You may also
# assume that the same calendar will remain in use for the foreseeable
# future.

'''
Problem:

  - Return the number of Friday the 13ths in a given year

     
  - Explicit requirements:
      - Calendar starts in 1752
  - Implicit requirements:
      - 
  - Questions
      - 

Examples/Test Cases:
    - print(friday_the_13ths(1986) == 1)      # True
    - print(friday_the_13ths(2015) == 3)      # True
    - print(friday_the_13ths(2017) == 2)      # True

Data Structure:
  - Input: integer
  - Output: integer
    
  - Intermediate: 

High-level strategies:
  - Iterate over every 13th of the month (12 iterations). If the day is
  a Friday, count it

Algorithm:  

  # Language agnostic for a non-programmer
  # Helper functions
  # Descriptive variable names
  # Run test cases through algo
  
  - Set year to arg, month to 1 and date to 13
  - While month < 12, check if it's a Friday, add 1 to month
  - If so, counter + 1
  - Return counter

'''
from datetime import date

def friday_the_13ths(year):
    month = 1
    count = 0
    while month <= 12:
        if date(year, month, 13).weekday() == 4:
            count += 1
        month += 1

    return count

print(friday_the_13ths(1986)) # 1
print(friday_the_13ths(2015)) # 3
print(friday_the_13ths(2017)) # 2