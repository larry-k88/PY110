# Write a function that takes a floating point number representing an
# angle between 0 and 360 degrees and returns a string representing that
# angle in degrees, minutes, and seconds. You should use a degree symbol
# (°) to represent degrees, a single quote (') to represent minutes, and
# a double quote (") to represent seconds. There are 60 minutes in a
# degree, and 60 seconds in a minute.

# Note: You can use the following constant to represent the degree
# symbol: DEGREE = "\u00B0"

'''
Problem:

    - Function that takes a float and returns a string which represents
    the angle in degrees, minutes and seconds

    - Input - float
    - Output - string
     
    - Explicit requirements:
        - Rules: 60 minutes in a degree
                 60 seconds in a minute
        - Input is in degrees and between 0 and 360
    - Implicit requirements:
        - 
    - Questions
        - How to handle floats outside the range

Examples/Test Cases:
    - print(dms(30) == "30°00'00\"")
    - print(dms(76.73) == "76°43'48\"")
    - print(dms(254.6) == "254°35'59\"" or dms(254.6) == "254°36'00\"")
    - print(dms(93.034773) == "93°02'05\"")
    - print(dms(0) == "0°00'00\"")
    - print(dms(360) == "360°00'00\"" or dms(360) == "0°00'00\"")
Test Cases: Further Exploration
    - print(dms(-1))   # 359°00'00"
    - print(dms(400))  # 40°00'00"
    - print(dms(-40))  # 320°00'00"
    - print(dms(-420)) # 300°00'00"

Data Structure:
    - str() to give the correct output
    -        

Algorithm:  

    - Calculate d, m and s from the argument
        - degree_value = int(degree)
        - minutes = (degrees - degree(value)) * 60
        - minutes_value = int(minutes)
        - seconds = (minutes - minutes(value) * 60
        - seconds_value = int(seconds_value)
    - f-string for output

'''
DEGREE = "\u00B0"
CONVERSION_VALUE = 60
def dms(degrees):
    normalised_degrees = degrees % 360 # Gives a value between 0 and 360
    degree_value = int(normalised_degrees)

    minutes = (normalised_degrees - int(normalised_degrees)) * CONVERSION_VALUE
    minutes_value = int(minutes)

    seconds = (minutes - minutes_value) * CONVERSION_VALUE
    seconds_value = int(seconds)

    return f'{degree_value}{DEGREE}{minutes_value:02}\'{seconds_value:02}"'

# All of these examples should print True
print(dms(30) == "30°00'00\"")
print(dms(76.73) == "76°43'48\"")
print(dms(254.6) == "254°35'59\"" or dms(254.6) == "254°36'00\"")
print(dms(93.034773) == "93°02'05\"")
print(dms(0) == "0°00'00\"")
print(dms(360) == "360°00'00\"" or dms(360) == "0°00'00\"")

print(dms(-1))   # 359°00'00"
print(dms(400))  # 40°00'00"
print(dms(-40))  # 320°00'00"
print(dms(-420)) # 300°00'00"
print(dms(-40.5)) # 319°30'00"
