# You are given a list of dictionaries, where each dictionary represents
# a student. Write a function that takes this list and returns a new 
# list containing the names of all students who have an average score of
# 85 or higher. The names in the returned list should be in uppercase.
# You must use a list comprehension to solve this.

# Function signature
def get_average(scores):
    return sum(scores) / len(scores)

def get_honors_students(students):
    return [student['name'].upper()
            for student in students
            if get_average(student['scores']) >= 85]

# Example Data
students = [
    {'name': 'Alice', 'scores': [90, 85, 88]},
    {'name': 'Bob', 'scores': [78, 80, 82]},
    {'name': 'Charlie', 'scores': [95, 89, 92]},
    {'name': 'Diana', 'scores': [82, 85, 80]},
]

# Expected Output
print(get_honors_students(students))
# Expected output: ['ALICE', 'CHARLIE']