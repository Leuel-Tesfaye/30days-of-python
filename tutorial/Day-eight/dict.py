
#?  A dictionary is a collection of unordered, mutable paired (key: value) data type.
#! when do we use dictionary in real world projects 
# 1, Dictionaries can be used to represent records in a database-like manner.users = {users = {
   # 'user1': {'name': 'Alice', 'age': 25, 'email': 'alice@example.com'},

# 2:  When working with APIs, responses are often in the form of JSON (JavaScript Object Notation), which can be easily represented using Python dictionaries.
#? api_response = {
# ?    'status': 'success',
# ?    'data': {'user_id': 123, 'username': 'john_doe'}
# ?}

#! creating a dictionary 
dict = {
    'Username: ' : 'prince',
    'Email:' : 'princeHope@gmail.com',
    'Password:' : 'password'
}
print ('user information :' , dict)

# dictionary length 
print(len(dict))

#? Accessing dictionary items 

person = {
    'first_name':'prince',
    'last_name':'Hope',
    'age':24,
    'country':'Ethiopia',
    'is_marred':False,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
    }

print(person['first_name'])
print(person['last_name'])
print(person['age'])
# Accessing an item by key name raises an error if the key does not exist.
# so to avoid this error we use get () method because get methods return none if key does not exist 

print(person.get('skills'))
print(person.get('address'))
print(person.get('hobbies'))

# Adding items to a dictionary 
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
dct['key5'] = 'value 5'
print(dct)

# modifying items in a dictionary 
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
dct['key1'] = 'value-one'
print('The modified version of dict :' , dct)

#! Removing Key and Value Pairs from a Dictionary
# pop(key): removes the item with the specified key name:
# popitem(): removes the last item
# del: removes an item with specified key name

item = {
    'item1' : 'item-one',
    'item2' : 'item-two',
    'item3' : 'item-three',
    'item4' : 'item-four',
}
print(item.pop('item1'))
print(item.popitem()) # removes the last item 

# getting dictionary as a list 
fruit = {
    'fruit1' : 'Mango',
    'fruit2' : 'Banana',
    'fruit3' : 'Apple',
    'fruit4' : 'Orange',
}
print(fruit.values())