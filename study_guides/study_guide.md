# Study Guide for PY119

+ [str methods: index, find, split, strip, join, replace, upper, lower, capitalize](#str-methods-index-find-split-strip-join-replace-upper-lower-capitalize)  
+ [list methods : append, extend, insert, remove, pop, clear, index, count, sort, reverse, copy](#list-methods--append-extend-insert-remove-pop-clear-index-count-sort-reverse-copy)  
+ [dict methods : keys, values, items, get, setdefault, update, pop, popitem, clear](#dict-methods--keys-values-items-get-setdefault-update-pop-popitem-clear)  
+ [set methods: add, update, remove, clear, union, intersection, difference, issubset, issuperset, isdisjoint](#set-methods-add-update-remove-clear-union-intersection-difference-issubset-issuperset-isdisjoint)  
+ [frozenset methods: union, intersection, difference, issubset, issuperset, isdisjoint](#frozenset-methods-union-intersection-difference-issubset-issuperset-isdisjoint)  
+ [tuple methods: count, index, unpacking](#tuple-methods-count-index-unpacking)  
+ [range and enumerate - Understanding of how to create and use range objects and enumerate for indexing during iteration.](#range-and-enumerate---understanding-of-how-to-create-and-use-range-objects-and-enumerate-for-indexing-during-iteration)  
+ [The built-in functions sum and all.](#the-built-in-functions-sum-and-all)  
+ [Conditional statements (if, elif, else)](#conditional-statements-if-elif-else)  
+ [Iteration using for loops, break, continue](#iteration-using-for-loops-break-continue)  
+ [Sorting lists using the sorted function and list.sort method](#sorting-lists-using-the-sorted-function-and-listsort-method)  
+ [Custom sorting using the key parameter and reverse sorting using the reverse parameter](#custom-sorting-using-the-key-parameter-and-reverse-sorting-using-the-reverse-parameter)  
+ [Comprehensions](#comprehensions)  
+ [Nested data structures and nested iteration](#nested-data-structures-and-nested-iteration)  
+ [Shallow and deep copy](#shallow-and-deep-copy)  
+ [Discuss a function's use and purpose (a "user-level" description) instead of its implementation](#discuss-a-functions-use-and-purpose-a-user-level-description-instead-of-its-implementation)  

## str methods: index, find, split, strip, join, replace, upper, lower, capitalize

+ `index`
    + Returns lowest index of a substring in the sequence
    + If the value isn't present: `ValueError`

            string = 'hello'

            string.index('l')
            --> 2

            string.index('M')
            --> ValueError: substring not found
        
    + Optional arguments are *start* and *stop* values
    + Returns lowest index of a substring at or after *start* and before *stop*, relative to the whole string

            string.index('l', 3) # finds the index of the 2nd 'l' (i.e. checks 'lo')
            --> 3

            string.index('o', 0, 4)
            --> ValueError: substring not found

+ `find`
    + Returns lowest index of a substring in the sequence
    + If the value isn't present: `-1` 
    
            string = 'hello'

            string.find('l')
            --> 2

            string.find('M')
            --> -1

    + Optional arguments are *start* and *stop* values
    + Returns lowest index of a substring at or after *start* and before *stop*

            string.find('l', 3)
            --> 3

            string.find('o', 0, 4)
            --> -1

    + Don't use `find()` to check if substring exists in the string - use `in`

            'llo' in string
            --> True

+ `split`
    + Breaks down a string into a list of substrings using the argument as the delimiter
    + If no argument given, it splits at one or more whitespace characters. But if a space is the separator, it splits only at spaces
    + Whitespace refers to spaces as well as chars like `\t` and `\n\`

            'fairy  god  mother'.split()
            --> ['fairy', 'god', 'mother'] # multiple spaces treated as one

            'fairy  god  mother'.split(' ')
            --> ['fairy', '', 'god', '', 'mother'] # multiple spaces treated separately 

    + A second argument can limit the number of splits (using `None` if necessary)

            'fairy  god  mother'.split(None, 2)
            --> ['fairy', 'god', 'mother']

    + You cannot split a string with an empty string as a separator (`''`), use `list` or `tuple`

            'fairy  god  mother'.split('')
            --> ValueError: empty separator

            list('fairy')
            --> ['f', 'a', 'i', 'r', 'y']
        + Third

+ `strip`
    + Removes whitespace from beginning and end (`lstrip()` and `rstrip()` remove leading/trialling whitespace respectively)
    + A string can be passed as an argument - NB the argument is not a prefix or suffix: any combination of the chars will be removed

                '      hello      '.strip()
                --> hello

                'www.example.com'.rstrip('ocm.')
                --> www.example

+ `join`
    + Opposite of `split` - takes a string and uses it as glue to join the iterable together

            '--'.join(['fairy', 'god', 'mother'])
            --> 'fairy--god--mother'

    + Elements in the iterable need to be string, otherwise TypeError

            '--'.join([1, 2, 3])
            --> TypeError: sequence item 0: expected str instance, int found
    
        + Can be overcome using a list comprehension

                '--'.join([str(num) for num in [1, 2, 3]])
                --> '1--2--3'

+ `replace`
    + Can substitute a substring within a string
    + 1st argument is the old substring, 2nd is the new substring

            '££45,000'.replace('£', '$')
            --> $$45,000

    + 3rd argument (optional) specifies how many replacements to do (no arg or a negative results in all being done)

            '££45,000'.replace('£', '$', 1)
            --> $£45,000
        + Third

+ `upper`
    + Transforms all characters to uppercase, no effect if already in that case

            'wishing WELL'.upper()
            --> WISHING WELL

+ `lower`
    + Transforms all characters to lowercase, no effect if already in that case

            'WISHING well'.lower()
            --> wishing well

+ `capitalize`
    + First character uppercase, rest lowercase
    + `swapcase()` inverts the case of each character

            'wishing WELL'.capitalize()
            --> Wishing well

            'wishing WELL'.swapcase()
            --> WISHING well

## list methods : append, extend, insert, remove, pop, clear, index, count, sort, reverse, copy

+ `append`
    + Adds an object to the end of a list
    
            cats = ['Lenny', 'Nora']
            cats.append('Bear')
            --> ['Lenny', 'Nora', 'Bear']

            cats = ['Lenny', 'Nora']
            cats.append(['Bear', 'Rosie'])
            --> ['Lenny', 'Nora', ['Bear', 'Rosie']] # Note the nested list

+ `extend`
    + Appends an iterable to the end of a list

            cats = ['Lenny', 'Nora']
            cats.extend(['Bear', 'Rosie'])
            --> ['Lenny', 'Nora', 'Bear', 'Rosie']

+ `insert`
    + Adds an object prior to the index position - if the index is greater than the length, it is added at the end

            cats = ['Lenny', 'Nora']
            cats.insert(1, 'Bear')
            --> ['Lenny', 'Bear', 'Nora']

+ `remove`
    + Removes the first occurrence of the value - if not present, ValueError

            cats = ['Lenny', 'Nora', 'Bear']
            cats.remove('Nora)
            --> ['Lenny', 'Bear']

            cats.remove('Sheldon')
            --> ValueError: list.remove(x): x not in list  

+ `pop`
    + Removes the value at the index - removes last item if no index given
    + Empty lists will raise IndexError

            cats = ['Lenny', 'Bear']
            cats.pop(0)
            --> Lenny # cats = ['Rosie']

            cats.pop()
            --> Rosie # cats = []

            cats.pop()
            --> IndexError: pop from empty list
            
        + `pop` returns the value it removes

+ `clear`
    + Empties the list

            cats = ['Lenny', 'Bear']
            cats.clear()
            --> []

+ `index`
    + Returns lowest index of a object in the list
    + If the object isn't present: `ValueError`

            cats = ['Lenny', 'Nora', 'Bear', 'Rosie', 'Lenny']

            cats.index('Bear')
            --> 2

            cats.index('Sheldon')
            --> ValueError: 'Sheldon' is not in list
        
    + Optional arguments are *start* and *stop* values
    + Returns lowest index of the value at or after *start* and before *stop*, relative to the whole list

            cats.index('Lenny') # 
            --> 0   
            
            cats.index('Lenny', 1) # search starts at 1, finds 'Lenny' at index 4
            --> 4

            cats.index('Lenny', 1, 3)
            --> ValueError: 'Lenny' is not in list


+ `count`
    + Counts the number of occurrences of an object, returns 0 if not present

            cats = ['Lenny', 'Nora', 'Bear', 'Rosie', 'Lenny']
            cats.count('Lenny)
            --> 2

+ `sort`
    + Sorts a list in place (mutates) - can deal with numbers anything else that it can evaluate (e.g. `a > b` is a valid expression)
    + If it cannot evaluate a comparison, TypeError

            cats = ['Lenny', 'Nora', 'Bear', 'Rosie', 'Lenny']
            cats.sort()
            --> ['Bear', 'Lenny', 'Lenny', 'Nora', 'Rosie']

            cats = ['Bear', 'Lenny', 'Lenny', 'Nora', 'Rosie', 5]
            cats.sort()
            --> TypeError: '<' not supported between instances of 'int' and 'str'

            cats = ['Bear', 'Lenny', 'Lenny', 'Nora', 'Rosie', '5']
            cats.sort()
            --> ['5', 'Bear', 'Lenny', 'Lenny', 'Nora', 'Rosie']


+ `reverse`
    + Second
        + Third

+ `copy`
    + Second
        + Third


## dict methods : keys, values, items, get, setdefault, update, pop, popitem, clear

+ `keys`
    + Second
        + Third

+ `values`
    + Second
        + Third

+ `items`
    + Second
        + Third

+ `get`
    + Second
        + Third

+ `setdefault`
    + Second
        + Third

+ `update`
    + Second
        + Third

+ `pop`
    + Second
        + Third

+ `popitem`
    + Second
        + Third

+ `clear`
    + Second
        + Third


## set methods: add, update, remove, clear, union, intersection, difference, issubset, issuperset, isdisjoint

+ `add`
    + Second
        + Third

+ `update`
    + Second
        + Third

+ `remove`
    + Second
        + Third

+ `clear`
    + Second
        + Third

+ `union`
    + Second
        + Third

+ `intersection`
    + Second
        + Third

+ `difference`
    + Second
        + Third

+ `issubset`
    + Second
        + Third

+ `issuperset`
    + Second
        + Third

+ `isdisjoint`
    + Second
        + Third


## frozenset methods: union, intersection, difference, issubset, issuperset, isdisjoint

+ `union`
    + Second
        + Third

+ `intersection`
    + Second
        + Third

+ `difference`
    + Second
        + Third

+ `issubset`
    + Second
        + Third

+ `issuperset`
    + Second
        + Third

+ `isdisjoint`
    + Second
        + Third


## tuple methods: count, index, unpacking

+ `count`
    + Second
        + Third

+ `index`
    + Second
        + Third

+ `unpacking`
    + Second
        + Third


## range and enumerate - Understanding of how to create and use range objects and enumerate for indexing during iteration.

+ `range`
    + Second
        + Third

+ `enumerate`
    + Second
        + Third

## The built-in functions sum and all.

+ `sum`
    + Second
        + Third

+ `all`
    + Second
        + Third


## Conditional statements (if, elif, else)

+ `if`
    + Second
        + Third

+ `elif`
    + Second
        + Third

+ `else`
    + Second
        + Third

## Iteration using for loops, break, continue

+ `for` loops
    + Second
        + Third

+ `break`
    + Second
        + Third

+ `continue`
    + Second
        + Third


## Sorting lists using the sorted function and list.sort method

+ `sorted`
    + Second
        + Third

+ `list.sort()`
    + Second
        + Third


## Custom sorting using the key parameter and reverse sorting using the reverse parameter

+ Custom Sorting
    + Second
        + Third

+ Reverse Sorting
    + Second
        + Third


## Comprehensions

+ Comprehensions
    + Second
        + Third


## Nested data structures and nested iteration

+ Nested Structures
    + Second
        + Third

+ Nested Iteration
    + Second
        + Third


## Shallow and deep copy

+ Shallow Copy
    + Second
        + Third

+ Deep Copy
    + Second
        + Third


## Discuss a function's use and purpose (a "user-level" description) instead of its implementation

+ Function Use
    + Second
        + Third

+ Function Purpose
    + Second
        + Third
