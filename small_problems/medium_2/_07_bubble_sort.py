# Bubble Sort is one of the simplest sorting algorithms available. It is
# not an efficient algorithm, so developers rarely use it in real code.
# However, it is an excellent exercise for student developers. In this
# exercise, you will write a function that sorts a list using the bubble
# sort algorithm.

# A bubble sort works by making multiple passes (iterations) through a
# list. On each pass, the two values of each pair of consecutive
# elements are compared. If the first value is greater than the second,
# the two elements are swapped. This process is repeated until a
# complete pass is made without performing any swaps. At that point, the
# list is completely sorted.

# Write a function that takes a list as an argument and sorts that list
# using the bubble sort algorithm described above. The sorting should be
# done "in-place" -- that is, the function should mutate the list. You
# may assume that the list contains at least two elements.

'''
Problem:

  - Take a list and sort based on the bubble algorithm

     
  - Explicit requirements:
      - Mutate the list
      - Minimum 2 elements
  - Implicit requirements:
      - Integers, strings
  - Questions
      - Can integers be negative?
      - For strings, case sensitive?

Examples/Test Cases:
    - lst1 = [5, 3]
    - bubble_sort(lst1)
    - print(lst1) #[3, 5]

    - lst2 = [6, 2, 7, 1, 4]
    - bubble_sort(lst2)
    - print(lst2) #[1, 2, 4, 6, 7]

    - lst3 = ['Sue', 'Pete', 'Alice', 'Tyler', 'Rachel',
    -         'Kim', 'Bonnie']
    - bubble_sort(lst3)

    - print(lst3) # ["Alice", "Bonnie", "Kim", "Pete",
                    "Rachel", "Sue", "Tyler"]

Data Structure:
  - Input: list
  - Output: list (ordered)
    
  - Intermediate: int to count the swaps

High-level strategies:
  - Iterate over 2 consecutive items and compare them - swap them if necessary
  and count the swap; if not necessary, carry on. If swaps is none, finish

Algorithm:  
    
  - Set swaps = 0
  - Iterate over indexes

'''
def bubble_sort(lst):
    while True:
        swapped = False
        for i in range(1, len(lst)):
            if lst[i - 1] > lst[i]:
                lst[i - 1], lst[i] = lst[i], lst[i -1]
                swapped = True
        if not swapped:
            break    

lst1 = [5, 3]
bubble_sort(lst1)
print(lst1)         # [3, 5]

lst2 = [6, 2, 7, 1, 4]
bubble_sort(lst2)
print(lst2)         # [1, 2, 4, 6, 7])

lst3 = ['Sue', 'Pete', 'Alice', 'Tyler', 'Rachel', 'Kim', 'Bonnie']
bubble_sort(lst3)
print(lst3) # ["Alice", "Bonnie", "Kim", "Pete", "Rachel", "Sue", "Tyler"]