# A triangle is classified as follows:

# Right: One angle is a right angle (exactly 90 degrees).
# Acute: All three angles are less than 90 degrees.
# Obtuse: One angle is greater than 90 degrees.

# To be a valid triangle, the sum of the angles must be exactly 180
# degrees, and every angle must be greater than 0. If either of these
# conditions is not satisfied, the triangle is invalid.

# Write a function that takes the three angles of a triangle as
# arguments and returns one of the following four strings representing
# the triangle's classification: 'right', 'acute', 'obtuse', or 'invalid'.

# You may assume that all angles have integer values, so you do not
# have to worry about floating point errors. You may also assume that the
# arguments are in degrees.

'''
Problem:

  - {Rewrite in own words}

     
  - Explicit requirements:
      - Each angle must be greater than 0
      - Total angles must equal 180
      - Angles are integers and in degrees
      - Rules for types are as above
  - Implicit requirements:
      - 
  - Questions
      - 

Examples/Test Cases:
    - print(triangle(60, 70, 50) == "acute")      # True
    - print(triangle(30, 90, 60) == "right")      # True
    - print(triangle(120, 50, 10) == "obtuse")    # True
    - print(triangle(0, 90, 90) == "invalid")     # True
    - print(triangle(50, 50, 50) == "invalid")    # True

Data Structure:
  - Input: 3x integers
  - Output: String
    
  - Intermediate: use `any`

High-level strategies:
  - Check for validity and return 'invalid' if appropriate. Check for 
  right, then obtuse, then else is acute

Algorithm:  

  # Language agnostic for a non-programmer
  # Helper functions
  # Descriptive variable names
  # Run test cases through algo
  
  - If not sum(angles) = 180 or any(angles) = 0, invalid
  - If any(angles) = 90 (right)
  - If any(angles) > 90 (obtuse)
  - Else acute 

'''

def triangle(ang1, ang2, ang3):
    angles = (ang1, ang2, ang3)
    if 0 in angles or sum(angles) != 180:
        return 'invalid'

    if 90 in angles:
        return 'right'
    if max(angles) > 90:
        return 'obtuse'
    return 'acute'

print(triangle(60, 70, 50))  # acute
print(triangle(30, 90, 60))  # right
print(triangle(120, 50, 10)) # obtuse
print(triangle(0, 90, 90))   # invalid
print(triangle(50, 50, 50))  # invalid