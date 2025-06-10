# One of the most frequently used real-world string operations is that
# of "string substitution," where we take a hard-coded string and modify
# it with various parameters from our program.

# Given the object shown below, print the name, age, and gender of each
# family member: '(name) is a (age)-year-old (male or female)'

munsters = {
    'Herman':  {'age': 32,  'gender': 'male'},
    'Lily':    {'age': 30,  'gender': 'female'},
    'Grandpa': {'age': 402, 'gender': 'male'},
    'Eddie':   {'age': 10,  'gender': 'male'},
    'Marilyn': {'age': 23,  'gender': 'female'},
}

for family_member, info in munsters.items():
    print(f'{family_member} is a {info['age']}-year-old {info['gender']}.')  



