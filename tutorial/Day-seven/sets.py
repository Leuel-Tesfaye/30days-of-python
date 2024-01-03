
#? set is a collection of unordered and un-indexed distinct elements. 
# In python sets used to store unique items and it's possible to find the union, intersection, difference , symmetric difference, subset and super set.

 #! creating a set syntax 

st = {'item1', 'item2', 'item3'}

#? checking an item in a set 
fruit = {'Banana', 'Mango', 'Apple', 'Orange', 'Lemon'}
print('Does the set fruit contain this item :', 'Apple' in fruit)

#? adding an item in a set
# In sets we can't change the items but we can add items in the set using add() 
fruit = {'Banana', 'Mango', 'Apple', 'Orange', 'Lemon'}
fruit.add('Avocado')
print(fruit)

# we can add multiple items using update () 
items = {'item1', 'item2', 'item3'}
items.update(['item4', 'item5', 'item6'])
print('List of items updated :', items)

# removing an item from a set 
items.remove('item3')
print(items)

# removing random item from the set using pop() 
items.pop()
print(items)

#! joining sets 
# we can join two sets using union () or update () methods 

st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item5', 'item6', 'item7', 'item8'}
united_set = st1.union(st2)
print('The union of set1 and set2 is :', united_set) 

#? finding intersection items 
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item3', 'item2'}
inter = st1.intersection(st2)
print('The intersection items are :' , inter)
