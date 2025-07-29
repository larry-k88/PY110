# Our countdown to launch isn't behaving as expected. Why? Change the
# code so that our program successfully counts down from 10 to 1 before
# launching.

''' `decrease` function doesn't update the variable `counter` - all it does it
create a new variable that is one less than the value passed in, and returns 
it. We need to capture this return value outside of the function
def decrease(counter):
    return counter - 1

counter = 10

for _ in range(10):
    print(counter)
    decrease(counter)
'''

def decrease(counter):
    return counter - 1

counter = 10

for _ in range(10):
    print(counter)
    counter = decrease(counter) 
# captures the return value of the function and updates the variable with it

print('LAUNCH!')

# Removes the decrease function
# counter = 10

# for _ in range(10):
#     print(counter)
#     counter -= 1

# print('LAUNCH!')