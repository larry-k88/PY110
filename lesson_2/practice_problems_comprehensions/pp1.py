# Compute and display the total age of the family's male members. Try
# working out the answer two ways: first with an ordinary loop, then with
# a comprehension. Result should be `444`

munsters = {
    'Herman':  {'age': 32,  'gender': 'male'},
    'Lily':    {'age': 30,  'gender': 'female'},
    'Grandpa': {'age': 402, 'gender': 'male'},
    'Eddie':   {'age': 10,  'gender': 'male'},
    'Marilyn': {'age': 23,  'gender': 'female'},
}

# Loop

total_male_age = 0
for person in munsters.values():
    if person['gender'] == 'male':
        total_male_age += person['age']

print(total_male_age)

# comprehension

male_ages = [person['age']
        for person in munsters.values()
        if person['gender'] == 'male']

print(sum(male_ages))