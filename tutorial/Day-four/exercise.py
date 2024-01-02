
# Declare a list with more than 5 items
items = ['prince', 'Hope', '24', 'Programmer','Ethiopian', 'Ambitious']
print(items)

#? Find the length of your list
print(len(items))

#? Get the first item, the middle item and the last item of the list
first_item = items[0]
middle_item = items[2]
last_item = items[-1]

print('First items is :', first_item)
print('Middle item is :', middle_item)
print('Last Item is :' , last_item)

# Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
IT_companies = [ 'Facebook', 'Google', 'Microsoft', 'Apple', 'Oracle' ]

# Print the number of companies in the list
print(len(IT_companies))

# Print the list after modifying one of the companies
IT_companies = [ 'Facebook', 'Google', 'Microsoft', 'Apple', 'Oracle' ]
IT_companies [0] = 'Amazon' 
print(IT_companies)

# Add an IT company to it_companies
IT_companies.append('IBM')
print(IT_companies)

# Insert an IT company in the middle of the companies list
IT_companies.insert(1, 'Samsung')
print(IT_companies)

