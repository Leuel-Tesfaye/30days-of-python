
#? Tuples : are a collection of datatypes which is ordered and immutable. 
# once a tuple is created we can't change it's values 
# we can't use add , insert , remove methods in tuple because it's nature is immutable.
# This is particularly useful when a function needs to return more than one piece of information.
        #? Example :
        #  def get_user_info() 
        # return username, email, age
        # user_info = get_user_info () 
        # username , email , age = user_info

# example 2 : i might use tuples to represent fixed collection of coordinates (x,y,z)

# creating empty tuple : 
empty_tuple = () 

fruits =('Banana', 'Apple', 'orange', 'Mango', 'lemon')
print('The number of fruits is : ',len(fruits))
first_item = fruits[0]
print('The first item in a tuple is : ',first_item)

#slicing tuples 
countries = ('Ethiopia', 'canada', 'America', 'Australia', 'Belgium')
foreign_countries = countries[1:]
print('List of Foreign countries : ', foreign_countries)

# negative slicing 
countries = ('Ethiopia', 'canada', 'America', 'Australia', 'Belgium')
minus_one_countries = countries[-1]
print('The last country from the tuple:', minus_one_countries)

#? checking an item in a tuple 
items = ('item1', 'item2', 'item3', 'item4','item5')
check_item = 'item2' in items
print('Is item found in list of items :' , check_item)

#! deleting tuples 
#? It's not possible to delete a single item in a tuple but it's possible to delete the tuple using del.
items = ('item1', 'item2', 'item3', 'item4','item5')
del items 

