# Create an empty dictionary called dog
dog = {}

# Add name, color, breed, legs, age to the dog dictionary
dog = {
    'name' : 'Jacky',
    'color' : 'white',
    'breed' : 'German shepard',
    'legs' : 'Four',
    'age' : '5',
}

print('This are the attributes of my Dog: ', dog)

# ? Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary

student = {
    'first_name' : 'prince',
    'last_name': 'Hope',
    'gender': 'Male',
    'age': '24',
    'marital status': 'single',
    'skills': {'Html','Css', 'Javascript','React', 'Python'},
    'country': 'Ethiopia',
    'city': 'Addis Ababa',
}

# Get the length of the student dictionary
print(len(student))

# Get the value of skills and check the data type, it should be a list
print(student.values())