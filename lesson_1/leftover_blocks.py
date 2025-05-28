'''
Problem:    Write a program that takes an available number of blocks,
            uses them according to the rules below to build the tallest
            structure, and calculates the number of blocks remaining
            Input - integer, available blocks
            Output - integer, remaining blocks
            Explicit requirements:
                - No gaps between blocks
                - Blocks are cubes
                - Top layer is one block
                - A block in an upper layer must be supported by 4
                - A lower block can support more than one upper block

            Implicit requirements:
                - Number of blocks can only be positive
                - No blocks will return 0
                - Number of blocks (top to bottom): 1, 4, 9 etc. which 
                are the squares of the layer
            
            Qs:
                - How to deal with negatives/decimals?
                - What makes a row valid?

Examples/Test Cases:    print(calculate_leftover_blocks(0) == 0)  # True
                        print(calculate_leftover_blocks(1) == 0)  # True
                        print(calculate_leftover_blocks(2) == 1)  # True
                        print(calculate_leftover_blocks(4) == 3)  # True
                        print(calculate_leftover_blocks(5) == 0)  # True
                        print(calculate_leftover_blocks(6) == 1)  # True
                        print(calculate_leftover_blocks(14) == 0) # True

Data Structure:     Dictionary? Key = layer, value = number of blocks
                    {1 : 1, 2 : 4, 3 : 9}
                    List = list of squares  
                    [[x], 
                     [x, x, x, x, ]
                     [x, x, x, x, x, x, x, x, x]
                     ]      

Algorithm:  

    High Level:
        - Take the number of starting blocks and remove the number of
          blocks in each layer
        - When a negative number is reached, the answer is the previous
          number (unless the answer is 0)
    
    Programmatic:
        - Take the starting_number of blocks
        - Set the remaining_blocks of blocks to the starting_number
        - Set layer = 1
        - While the remaining_blocks > 0:
            - Loop through (layer ** 2) and subtract from remaining_blocks
            - Update remaining_blocks
            - Increment layer
        - If remaining_blocks drops below 0, return the layer (prior to
          incrementing)
        - If remaining_blocks is 0, return 0

'''

# def calculate_leftover_blocks(total_blocks):
#     remaining_blocks = total_blocks
#     current_layer = 1
#     while remaining_blocks > 0:
#         updated_remaining_blocks = remaining_blocks - (current_layer ** 2)
#         current_layer += 1
#         if updated_remaining_blocks < 0:
#             return remaining_blocks
#         remaining_blocks = updated_remaining_blocks
#     return 0

def calculate_leftover_blocks(total_blocks): # LSBot
    remaining_blocks = total_blocks
    current_layer = 1
    while remaining_blocks > 0:
        blocks_needed = current_layer ** 2
        if remaining_blocks < blocks_needed:
            return remaining_blocks
        
        remaining_blocks -= blocks_needed
        current_layer += 1
    
    return 0


print(calculate_leftover_blocks(0) == 0)  # True
print(calculate_leftover_blocks(1) == 0)  # True
print(calculate_leftover_blocks(2) == 1)  # True
print(calculate_leftover_blocks(4) == 3)  # True
print(calculate_leftover_blocks(5) == 0)  # True
print(calculate_leftover_blocks(6) == 1)  # True
print(calculate_leftover_blocks(14) == 0) # True
