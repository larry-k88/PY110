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

            cats = ['Bear', 'Lenny', 'Lenny', 'Nora', 'Rosie', '5'] # number as a string
            cats.sort()
            --> ['5', 'Bear', 'Lenny', 'Lenny', 'Nora', 'Rosie']

        + `reverse=True` can be added as a keyword argument to reverse the order
    
    + a function or method can be added which overrides what values are compared as long as it returns a value and the expected argument is compatible with all elements in the list:
    
            list.sort(key=str.casefold) # a case-insensitive sort

            list.sort(key=int) # sort by numeric strings (converts to int first, then sorts)

            list.sort(key=str) # ensures values are of the same type before sorting

+ `reverse`
    + Reverse a list in place (mutates)

            cats = ['Lenny', 'Nora', 'Bear', 'Rosie', 'Lenny']
            cats.reverse()
            --> ['Lenny', 'Rosie', 'Bear', 'Nora', 'Lenny']

+ `copy`
    + Creates an actual copy of the dictionary, unlike assignment (`list1 = list2`) which only creates a reference

            data = {'name': 'Srdjan', 'city': 'Belgrade'}
            data1 = data

            data['country'] = 'Serbia'

            data --> {'name': 'Srdjan', 'city': 'Belgrade', 'country': 'Serbia'}
            data1 --> {'name': 'Srdjan', 'city': 'Belgrade', 'country': 'Serbia'}
            # both point to the same mutated list

    + vs. a shallow copy (mutable values will be updated in the copy)

            data = {'name': 'Srdjan', 'city': 'Belgrade'}
            data1 = data.copy()  
            
            data['country'] = 'Serbia'

            data --> {'name': 'Srdjan', 'city': 'Belgrade', 'country': 'Serbia'}
            data1 --> {'name': 'Srdjan', 'city': 'Belgrade'} # copy isn't mutated

## dict methods : keys, values, items, get, setdefault, update, pop, popitem, clear

+ `keys`
    + Isolates the keys which can then be transitioned into a list/tuple
    + The returned object is dynamic - it changes if the keys are changed:

            book = {'title': 'Dune', 'author': 'Frank Herbert', 'year': 1965}
            key_view = book.keys()
            key_view
            --> dict_keys(['title', 'author', 'year'])

            book['publisher'] = 'Chilton Books'
            key_view
            --> dict_keys(['title', 'author', 'year', 'publisher'])
        
        + Doesn't need `keys()` method invoked again to update the `dict_keys` object
        + Converting to a list/tuple *will* create a static snapshot

+ `values`
    + As above but focuses on the value in the dictionary
    + This examples shows how creating a list creates a static snapshot

            fruits = {'apple': 4, 'banana': 2}
            values_list = list(fruits.values())
            --> [4, 2]

            fruits['pear'] = 5
            values_list
            --> [4, 2] # doesn't update with the value `5`

+ `items`
    + As above but focuses on the key: value pairs in the dictionary (called items)
    + In this case, they pairs are already tuples
    + This examples shows how creating a tuple creates a static snapshot

            fruits = {'apple': 4, 'banana': 2}
            items_tuple = tuple(fruits.items())
            --> (('apple', 4), ('banana', 2))

            fruits['pear'] = 5
            items_tuple
            --> (('apple', 4), ('banana', 2)) # doesn't update with the item `'pear': 5`

+ `get`
    + Fetches a value based on the key
    + If it doesn't exist, it returns None (or whatever is set as `default`)

            fruits = {'apple': 4, 'banana': 2}
            fruits.get('pear')
            --> None

            fruits.get('pear', "Fruit doesn't exist")

+ `setdefault`
    + Similar to `get` in that it returns the value if the key exists
    + However, it creates a new key/pair value if the key doesn't exist, then returns the value

            fruits = {'apple': 4, 'banana': 2}
            fruits.setdefault('apple', 5)
            --> 4 # apple is a key so it's value is returned

            fruits.setdefault('pear', 5)
            --> 5 # pear is not a key, so a new key/value pair is created

            fruits
            --> {'apple': 4, 'banana': 2, 'pear': 5}

+ `update`
    + Used to merge one dictionary into another
    + Any duplicate keys: dictionary in the argument takes priority

            data = {'name': 'Steve', 'age': 'unknown'}

            new_data = {'city': 'London', 'age': 23}

            data.update(new_data)
            data
            --> {'name': 'Steve', 'age': 23, 'city': 'London'}

        + `age` has been updated
        + The `|=` operator does exactly the same thing

                data |= new_data

        + The `|` operator **merges** dictionaries, creating a new one:

                merged_data = data | new_data

+ `pop`
    + Removes a key/value pair and returns the value - useful when you want to use the value after deleting the key

            data = {'name': 'Steve', 'age': 'unknown'}
            data.pop('age')
            --> 'unknown'

        + If the key doesn't exist, a KeyError will be raised

                data = {'name': 'Steve', 'age': 'unknown'}
                data.pop('city')
                --> KeyError: 'city'

        + A default value can be provided to avoid this:

                data = {'name': 'Steve', 'age': 'unknown'}
                data.pop('city', 'Key not found')
                --> 'Key not found'

+ `popitem` 
    + Removes the last item (key/value pair) and returns it as a tuple

            data = {'name': 'Steve', 'age': 'unknown'}
            data.popitem()
            --> ('age', 'unknown')

        + Calling on an empty dictionary raises a KeyError

+ `clear`
    + Empties the dictionary
        
            data = {'name': 'Steve', 'age': 'unknown'}
            data.clear()
            --> {}


## set methods: add, update, remove, clear, union, intersection, difference, issubset, issuperset, isdisjoint

+ `add`
    + Adds an element to the set. If that element is already in it, it won't do anything

        names = {'Ben', 'Jerry'}
        names.add('Bill')
        --> {'Ben', 'Jerry', 'Bill'} # in any order

        names.add('Ben')
        --> {'Bill', 'Jerry', 'Ben'} # no change, except the order 

+ `update`
    + Similar to with dictionaries, it combines the sets (removing any duplicates)

            names = {'Ben', 'Jerry'}
            more_names = {'Ted'}

            names.update(more_names)
            --> {'Ted', 'Jerry', 'Ben'}
        
        + As sets have no duplicates, `more_names.update(names)` would have the same result

+ `remove`
    + Removes the element from the set

            names = {'Ben', 'Jerry'}

            names.remove('Ben')
            --> {'Jerry'}

        + If the element doesn't exist, KeyError. However `discard()` can be used which doesn't care if the element is in the set

+ `clear`
    + Empties the set
        
            names = {'Ben', 'Jerry'}
            data.clear()
            --> {}
+ `union`
    + Combines elements of 2 sets, can also use `|`
    + Does not mutate either set (unlike `set.update()` which mutates the first set)

            names1 = {'Ben', 'Jerry'}
            names2 = {'Bill', 'Ted'}

            names1.union(names2) # names1 | names2
            --> {'Ben', 'Jerry', 'Bill', 'Ted'}

+ `intersection`
    + Identifies common elements of 2 sets, can also use `&`
    + Does not mutate either set

            names1 = {'Ben', 'Jerry'}
            names2 = {'Ben', 'Ted'}

            names1.intersection(names2) # names1 & names2
            --> {'Ben'}

+ `difference`
    + Identifies elements in 1 set but not the other, can also use `-`
    + Does not mutate either set

            names1 = {'Ben', 'Jerry'}
            names2 = {'Ben', 'Ted'}

            names1.difference(names2) # names1 - names2
            --> {'Jerry'}
            
            names2.difference(names1) # names2 - names2
            --> {'Ted'}

+ `issubset`
    + All elements of the first are in the second, can also use `<=`
    + `<` can be used to check for proper subset (subset, but not equal)

+ `issuperset`
    + All elements of the second are in the first, can also use `>=`
    + `>` can be used to check for proper superset (superset, but not equal)

            names1 = {'Ben', 'Jerry'}
            names2 = {'Bill', 'Ted'}
            names3 = {'Ben'}

            names3.issubset(names1)
            --> True
            
            names3.issuperset(names1)
            --> False

            names3 <= names2
            --> False

            names3 >= names2
            --> False

            names2.issubset(names2)
            --> True
        
            names2.issuperset(names2)
            --> True
    
            names2 < names2
            --> False

+ `isdisjoint`
    + If 2 sets are disjoint, they have no common elements: their intersection is empty

            names1 = {'Ben', 'Jerry'}
            names2 = {'Bill', 'Ted'}

            names1.isdisjoint(names2)
            --> True

## frozenset methods: union, intersection, difference, issubset, issuperset, isdisjoint

+ A frozenset is an immutable set so any non-mutating methods or operators that are available for sets will work with frozensets.

+ Mutating methods that **cannot** be used are:
    + `add`, `remove`, `discard`, `pop` and `clear`

## tuple methods: count, index, unpacking

+ `count` and `index` methods identical to the [list methods](#list-methods--append-extend-insert-remove-pop-clear-index-count-sort-reverse-copy)

+ `unpacking`
    + A method to assign values from a tuple to multiple variables at the same time

            data = ('Ben', 25, 'flowerpot man')
            name, age, job = data

            name
            --> 'Ben'
            age
            --> 25
            job
            --> 'flowerpot man'

        + Unpacking can be done with other iterables such as lists. But as lists are mutable, the number of elements can change - this makes it hard as the number of variables must equal the number of elements in order to avoid errors.


## range and enumerate - Understanding of how to create and use range objects and enumerate for indexing during iteration.

+ `range`
    + Doesn't hold all of its numbers at once, it's an iterable that delivers them on demand, e.g. using the `list` function
    + Ranges are immutable but can be assigned to variables: `my_range = range(3)`
    + Operations supported include: slicing, iteration, `len()`, `count()`, `index()`, `min()`, `max()` but not concatenation.
    + Can take 1, 2 or 3 arguments - start, end, step (similar to a slice):

            list(range(3))
            --> [0, 1, 2]

            list(range(1, 3))
            --> [1, 2]

            list(range(1, 4, 2))
            --> [1, 3]

        + Negative step values generate numbers down from start to end
        + If the range cannot be generated, an empty list is the result

    + The elements can be indexed as with other sequences (`IndexError` if out of range):

            range(1, 3)[1] # value at index 1 in [1, 2]
            --> 2

    + Iterating over ranges is a useful way to perform something x number of times

            for _ in range(3): # This will print 'hi' 3 times
                print('Hi')

    + Ranges support the `count` and `index` methods:

            range(3, 10).count(5) # has values 3, 4, 5, 6, 7, 8, 9
            --> 1 # 5 appears once

            range(3, 10).index(5) # 5 is at index position 2
            --> 2

        + `count()` will only return `1` or `0` (similar to `5 in range(3, 10)`, except this returns a `True` or `False`)
        + `index()` will return a `ValueError` if the value is not in the range

    + Ranges support `start`, `end` and `stop` attributes - useful if you have a range object and you don't know what it represents:

            unknown_range = range(4, 42, 3)

            unknown_range.start
            --> 4

            unknown_range.stop
            --> 42

            unknown_range.end
            --> 3

        + If start/stop/end are omitted, the attributes return the default values

+ `enumerate`
    + This is a way of keeping track of an element *and* its position in the sequence
    + The argument is an iterable and it returns a new iterable, not a single tuple:

            data = ('Ben', 'Bill', 'Ted')
            for index, name in enumerate(data):
                print(f'{name} is at index {index})
        
            --> Ben is at index 0
            --> Bill is at index 1
            --> Ted is at index 2

        + Second line is an example of [tuple unpacking](#tuple-methods-count-index-unpacking)

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
