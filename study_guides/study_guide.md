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
    + Must be hashable objects (otherwise TypeError)
    + Avoid using floats as keys (issues with floating-point precision)
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
    + The argument can be a variable (same as when referencing an element)
    + If it doesn't exist, it returns None (or whatever is set as `default`)

            fruits = {'apple': 4, 'banana': 2}
            fruits.get('pear')
            --> None

            fruits.get('pear', "Fruit doesn't exist")

            key1 = 'apple'
            key2 = 'pear'

            fruits[key1]
            --> 4
            fruits[key2]
            --> KeyError: 'pear'

            fruits.get(key1)
            --> 4
            fruits.get(key2, "Fruit doesn't exist")
            --> Fruit doesn't exist

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

        + The `|` operator (or `**` operator) **merges** dictionaries, creating a new one:

                merged_data = data | new_data
                merged_data = {**data, **new_data}
                # Both produce the same result

            + `**` can also be used for packing/collecting (e.g. `**kwargs`)

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
    
    + Set items must be hashable (i.e. usually immutable)

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
+ It can only contain hashable objects (unlike tuples which can contain unhashable objects like lists) - this means they will **always** be hashable

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

    + The `*` operator (unary asterisk) can unpack the contents of heterogeneous operators:

            numbers = [1, 2]
            tup_1 = (3, 4)
            sequence = numbers + list(tup_1) # [1, 2, 3, 4]
     
            # Using *
     
            sequence = [*numbers, *tup_1]
            # [1, 2, 3, 4]           

    + Or to pass iterables as separate arguments:

            def test(num1, num2):
                # do something
    
            numbers = [1, 2]
            test(numbers[0], numbers[1]) # clunky
    
            # Using *
            test(*numbers)
    
    + Nested unpacking:
    
            numbers = [1, [2, 3, 4], 5]
            a, (b, c, d), e = numbers

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
    + Works with iterables that are entirely numeric - returns the sum of the values in the collection
    + With dictionaries, it will sum the keys (ignoring the values)

            num_dict = {1: 'a', 2: 'aa'}
            sum(num_dict)
            --> 3

            num_range = range(1, 3) # 1, 2
            sum(num_range)
            --> 3

+ `all`
    + Returns `True` if all elements are truthy, `False` otherwise
    + If none of the are falsy, it will also return`True` i.e. any empty collection

            all([2, True])
            --> True

            all([0, True])
            --> False

            all([])
            --> True # No element is falsy

    + Can be used to check if elements have a certain condition, e.g. in comprehensions

            numbers = [2, 5, 8, 10, 13]
            all([number % 2 == 0 for number in numbers])
            --> False

            numbers = [5, 13]
            all([number % 2 == 0 for number in numbers])
            --> False

            numbers = [2, 8, 10]
            all([number % 2 == 0 for number in numbers])
            --> True


## Conditional statements (if, elif, else)

+ `if`
    + Determines whether the condition is True
    + If it is, the indented block executes
    + If it isn't, the code resumes at the next non-indented line

+ `elif`
    + Only executes if the `if` statement is False

+ `else`
    + Executes if **all** the above conditions are False

+ Multiple `if` statements can be used to check condition independently - e.g. if more than one could be True and you want the indented code to run for each
+ An `if` followed by an `elif` means only one indented block would run - i.e. the conditions are mutually exclusive
    + `if/elif/else` gets a single choice from multiple options
    + multiple `if`s only get one option

## Iteration using for loops, break, continue

+ `for` loops
    + Work with all built-in collections (including strings)
    + Iterates over the items in the collection and does something with each
    + NB with sets, the order can be changed
    + NB with dictionaries, it iterates over the keys by default (use `dict.values()` to iterate over the values, or `dict.items()` for the pairs, with [tuple unpacking](#tuple-methods-count-index-unpacking) if necessary)
        + Third

+ `break`
    + Exits the nearest enclosing loop immediately
    + Useful if you don't want the code to continue after a certain condition is met
    + Used to emulate do/while loops - use `while` to keep the loop going and then use `break` to exit the loop when a condition is met:

            while True:
                # main loop

                answer = input('Play again? y/n')
                if answer in ('n', 'N'):
                    break

+ `continue`
    + Starts a new loop iteration by skipping the rest of the block (only of the nearest enclosing loop)
    + They can also be written with negated `if` conditions

            data = ('Ben', 'Bill', 'Ted')

            for name in data:
                if name[0] == 'T':
                    continue
                print(name)


            for name in data:
                if not name[0] == 'T':
                    print(name)

        + Both print `Ben` and `Bill` - both are fine


## Sorting lists using the sorted function and list.sort method

+ Sorting, like `min` and `max` rely on the element types being comparable (along with operators like `<` and `>`). Therefore using any of these methods/operations on mixed collections (e.g. strings and integers) will result in a `TypeError`

+ `sorted`
    + Non-destructive - returns a new list (non-mutating)
    + It can therefore be used with immutable objects like strings (produces a list)

            sorted('Ted')
            --> ['T', 'd', 'e']

        + Order depends on the "code point" in Unicode Standard: use `ord()` to get the value

                ord('T') # 84
                ord('e') # 101
                ord('d') # 100

+ `list.sort()`
    + Modifies the list in place (mutating) and returns `None`
    + Doesn't work on any other data type, only lists

            vowels = ['u', 'i', 'a', 'e', 'o']
            sorted_vowels = sorted(vowels) # need to capture the value
            print(vowels)         # ['u', 'i', 'a', 'e', 'o']
            print(sorted_vowels)  # ['a', 'e', 'i', 'o', 'u']
            
            vowels = ['u', 'i', 'a', 'e', 'o']
            vowels.sort()
            print(vowels)  # ['a', 'e', 'i', 'o', 'u']

## Custom sorting using the key parameter and reverse sorting using the reverse parameter

+ Custom Sorting
    + **First-class objects** (including functions) meet the following conditions:
        + Can be assigned to a variable or an element of a data structure
        + Can be passed as an argument to a function
        + Can be returned as the return value of a function
    + **Higher-order functions** take other functions as arguments or return functions
        + `list.sort()` and `sorted` are examples, and accept a function as an argument

    + The function object that is passed as an argument is done so via the `key` keyword - the function calls that function object on each object in the list - it is the return value of each of those calls that is used for comparison during the sorting process.

            data = ['Ben', 'Bill', 'Ted']
            sorted_data = sorted(data, key=len)
            --> ['Ben', 'Ted', 'Bill']

    + A custom function can be defined for use as the sorting key and that function can return a tuple, e.g.

            def person_key(person):
                name, age = person
                return (age, name)
        
        + This takes the argument (a tuple), unpacks it and turns it around

                person_key(('Ben', 23))
                --> (23, 'Ben')

        + To sort a list of tuples by age, this function can be passed as the key

                data = [('Ben', 23), ('Bill', 25), ('Ted', 21)]
                # sorted(data) would sort alphabetically by name only

                sorted(data, key=person_key)
                --> [('Ted', 21), ('Ben', 23), ('Bill', 25)]
                # sorts by age first, then alphabetically 

+ Reverse Sorting
    + Both options above accept the `reverse` keyword argument - when set to True, the list will descend

            sorted('Ted', reverse=True)
            --> ['e', 'd', 'T']


## Comprehensions

+ List Comprehensions
    + Shorthand for creating collections:

            [output_exp for item in existing_list if condition]

    + Transformations:
        + Creating a new list by changing (or not) each element of the old list

                nums = [1, 2, 3]
                [num**2 for num in nums]
                --> [1, 4, 9]

            + If there is no actual change in the value, it is called an 'identity transformation' (makes a shallow copy)

    + Filtering:
        + Uses the `if` condition to filter

                nums = [1, 2, 3]
                [num for num in nums if num % 2 == 1]
                --> [1, 3] # this is an identity transformation with a filter

    + Combination:

                nums = [1, 2, 3]
                [num**2 for num in nums if num % 2 == 1]
                --> [1, 9]
    
+ Set Comprehensions
    + Similar to lists but the output is an unordered set with no duplicates

+ Dictionary Comprehensions
    + Similar to lists but the output is a key_exp: value_exp pair

            data = ['Ben', 'Bill', 'Ted']
            {name: name.lower() for name in data}
            --> {'Ben': 'ben', 'Bill': 'bill', 'Ted': 'ted'}

+ Tuple Comprehensions do not exist!

+ The collection that is iterated over can be any iterable type, including ranges, frozensets, files

+ Don't use comprehensions unless you're using the return value (i.e. if printing, use a loop)

## Nested data structures and nested iteration

+ Nested Structures
    + These are collections within collections and can be accessed by chaining indexes:

            data = [['Bill', 'Ben'], ['Bill', 'Ted']]
            data[1][1]
            --> Ted
        
    + Updating elements looks like chained indexes, but it actually on index followed by a reassignment

            data = [['Bill', 'Ben'], ['Bill', 'Ted']]
            data[1][1] = 'Coo'
            
        + `data[1]` is the index part - gives `['Bill', 'Ted']`, so we have...
        + `['Bill', 'Ted'][1] = 'Coo'` which is reassigning second element (`'Ted'`) to `'Coo'`
        + This is destructive/mutating

    + Appending elements is the same - first part in the index, second is the appending part:

            data = [['Bill', 'Ben'], ['Bill', 'Ted']]
            data[1].append('Rufus')
            --> [['Bill', 'Ben'], ['Bill', 'Ted', 'Rufus']]

        + `data[1]` indexes and gives `['Bill', 'Ted']`, so we have...
        + `['Bill', 'Ted'].append('Rufus')` which mutates the list, added 'Rufus'
        + Note that it's possible to append another list, resulting in a 3-deep nested structure (e.g. `data[1].append([1989, 1991])`)

    + **Lists** can contain dictionaries, tuples, sets and frozensets

    + **Tuples** can contain lists, tuples, dictionaries, sets and frozensets

    + **Dictionaries** must have hashable keys, but values can be anything

    + **Sets** and **frozensets** can only contain collections that are hashable - cannot contain lists, dictionaries or other sets.

    + Using variables to reference inner collections:

            names = ['Bill', 'Ben']
            ages = [23, 25]
            data = [names, ages]
            --> [['Bill', 'Ben'], [23, 25]]

        + The list `data` contains *references* to lists `name` and `age`

                names = ['Bill', 'Ben']
                ages = [23, 25]
                data = [names, ages]

                names.append('Ted')
                data
                --> [['Bill', 'Ben', 'Ted'], [23, 25]]

        + Both `names` and `data[0]` reference the same object:

                data
                --> [['Bill', 'Ben', 'Ted'], [23, 25]]

                data[0].remove('Ted') # names.remove('Ted') has same effect
                
                --> [['Bill', 'Ben'], [23, 25]]

+ Nested Iteration
    + Start with the outer loop and assign the variable to the first element
    + The start the inner loop and process it completely
    + Then move to the second element of the outer loop and complete the inner loop again

    + These also appear in comprehensions as selection criteria: multiple selection criteria are similar to nested `if` statements

            colours = ['Red', 'Blue']
            modes = ['Car', 'Bus']

            [(colour, mode) for colour in colours for mode in modes]

## Shallow and deep copy

+ Shallow Copy
    + Creates a new copy of the object, but not of nested mutable objects (only references are copied)

            data = [['Bill', 'Ben'], ['Bill', 'Ted']]
            data_copy = data.copy()

            data_copy[0] = 'flowerpot men' # reflected in the copy only
            data_copy[1][1] = 'Rufus' # reflected in both

            data
            --> [['Bill', 'Ben'], ['Bill', 'Rufus']]
            data_copy
            --> ['flowerpot men', ['Bill', 'Rufus']]

    + Lists:
        + use `list` function - `list(lst)`
        + use slicing - `lst[:]`
        + use `copy()` - `lst.copy()` (works for lists, sets, frozensets and dictionaries)
        + `import copy` - `copy.copy(lst)` (works for all iterables and returns an object of the same type it was passed)

    + Dictionaries:
        + use `dict` function - `dict(dictionary)`
        + use `copy()` - `dictionary.copy()`
        + `import copy` - `copy.copy(dictionary)` 

+ Deep Copy
    + Creates new copy of the object and recursively copies all nested mutable objects (it still just creates references to immutable ones)
    + Modifying nested elements in the deep copy has no effect on the original
    + Requires a lot more processing than shallow copies
    + `import copy` - `copy.deepcopy(iterable)`


## Discuss a function's use and purpose (a "user-level" description) instead of its implementation

+ Function Use
    + This is how to use the function and can include what arguments it accepts and what it returns.
    + It does not contain details of the function body (e.g. how it gets from the arguments to the return value, this would be an 'implementation-level' description)

            def append_to(str1, str2):
                for char in str2:
                    str1 += char
                
                return str1

        + *The function accepts two strings as arguments and it returns a new string which is the result of appending the second string to the first*

+ Function Purpose
    + This is what the function is for:
        + *The function concatenates two strings*


+ For reference, an implementation-level description would be:
    + *The function takes two arguments, `str1` and `str2`. Inside the function, a `for` loop iterates through each character (`char`) of the second string argument, `str2`. In each iteration, the current `char` is appended to the first string, `str1`, using the `+=` operator. After the loop finishes, a new string referenced by `str1` is returned*

## Misc

+ Hashing
    + Hashable objects have a stable and *mostly* unique identifier - their 'hash value'
    + The `hash` function generates the value which remains constant for the duration of the objects life
    + 2 keys can have the same hash values (a *hash collision*) but Python resolves these invisibly
    + Immutable objects are hashable but only if all elements within are hashable

            data = ('phones', 4, 'u')
            # hashable tuple as the elements are all hashable (still immutable)

            data = ('phones', 4, ['u', 'U'])
            # unhashable tuple as one element is an unhashable list (still immutable)

    + Any mutable object is unhashable