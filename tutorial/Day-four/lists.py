
# Lists : is a collection which is ordered and mutable. allows duplicate members. 
 #? Tuple : is a collection of data which is ordered and immutable. allows duplicate members 
# set : is a collection which is unordered, un-indexed and immutable, but we can add new items to the set duplicate members are not allowed 
# Dictionary : is collation which is ordered and mutable but don't allows duplicate member. 

#! In python we can create list in two ways : 
empty_list = list() 
print (len(empty_list))

#! the second way is 
list = []
print(len(list))

list_techs = ['html', 'css', 'javascript', 'python', 'React']
print('List of techs :', list_techs)

#! lists can have items with different data types : 

items = ['prince', '24', {'country': 'Ethiopia', 'City': 'Addis Ababa'}, ]
print(items)

# Accessing List Items Using Positive Indexing
print(items[0])

## Accessing List Items Using negative Indexing
print(items[-1])

#! slicing items from a list

fruits = ['banana', 'orange', 'mango', 'lemon']
print(fruits[0:2])

#? modifying items in a list 
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits [0] = 'apple'
print('fruits', fruits)

#! checking items in a list 
fruits = ['banana', 'orange', 'mango', 'lemon']
does_exist = 'banana' in fruits
print(does_exist)

#? adding items in a list 
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.append('apple')
print(fruits)

#! inserting items in a list 

countries = ['Ethiopia', 'kenya', 'Japan', 'England']
countries.insert(2, 'sudan')
print('List of countries: ',countries)

#? removing items from a list 
countries = ['Ethiopia', 'kenya', 'Japan', 'England']
countries.remove('Ethiopia')
print(countries)

#! removing items from a list using their index (pop method)
skills = ['communication', 'analytical skill', 'microsoft office']
skills.pop(2)
print('List of skills :', skills)
