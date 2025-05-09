'''
Write a program that solicits six (6) numbers from the user and prints a
message that describes whether the sixth number appears among the first
five.

Problem:    Ask the user for 6 numbers. Message is printed which states
            if the 6th number appears in the first 5.
            Input - 6x inputs from user (NB inputs will be strings)
            Output - f-string: message depends on the inputs
            Explicit requirements:
                - Ask user for 1 number, 6 times
                - Message should change depending on the 6th number

            Implicit requirements:
                - Numbers should be stored as in a collection

Examples/Test Cases:    Enter the 1st number: 25
                        Enter the 2nd number: 15
                        Enter the 3rd number: 20
                        Enter the 4th number: 17
                        Enter the 5th number: 23
                        Enter the last number: 17

                        17 is in 25,15,20,17,23.

                        Enter the 1st number: 25
                        Enter the 2nd number: 15
                        Enter the 3rd number: 20
                        Enter the 4th number: 17
                        Enter the 5th number: 23
                        Enter the last number: 18
                        
                        18 isn't in 25,15,20,17,23.

Data Structure:     Input will be a string
                    Strings can be stored in a collection (set - no duplicates)
                    `in` builtin function to check set membership
                    `if` clause to print one of 2 messages
                    f-strings to interpolate the inputs       

Algorithm:  

    Pseudocode
    - Get 5x inputs from the user
    - Add each input to a set
    - Get the 6th number and set it to a variable
    - Check if the variable is in the set
        - If so, print a message
        - Else, print a different message

'''
numbers_string = []
numbers_string.append(input('Enter the 1st number: '))
numbers_string.append(input('Enter the 2nd number: '))
numbers_string.append(input('Enter the 3rd number: '))
numbers_string.append(input('Enter the 4th number: '))
numbers_string.append(input('Enter the 5th number: '))

sixth_number = input('Enter the last number: ')

if sixth_number in numbers_string:
    print()
    print(f'{sixth_number} is in {','.join(numbers_string)}.')

else:
    print()
    print(f'{sixth_number} isn\'t in {','.join(numbers_string)}.')

'''
Further exploration:
Using the `if` block to search for a number that satisfies a condition 
will not work here as the inputs are all strings. In order to make this 
work, we would need to convert the inputs to integers first, then check 
the condition
'''