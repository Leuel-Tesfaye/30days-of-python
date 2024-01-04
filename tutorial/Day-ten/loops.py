
#! loops 
# Life is full of routines. In programming we also do lots of repetitive tasks.
# There are two types of loops in python : while loops and for loops 

#! while loops 
# It is used to execute a block of statements repeatedly until a given condition is satisfied. 
count = 0 
while count < 5:
    # print(count)
    count = count + 1

# the following is while with else condition. 
# count = 0
# while count < 5:
#     # print(count)
#     count = count + 1
# else:
#     print(count)

#! For Loop
 #  Loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).
# numbers = [0,1,2,3,4,5,6]

# for number in numbers :
#     # print(number)

language = 'python '

for letter in language:
    print(letter)

# ? for loops in dictionary 
    person = {
    'first_name':'prince',
    'last_name':'hope',
    'age':250,
    'country':'Finland',
    'is_marred':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
}
    # for key in person :
    #     print(key)
for key, value in person.items() :
    # print(key, value)

# ! For Else
 numbers = [0,1,2,3,4,5,6]
 for number in numbers : 
    print(number)
else : 
   print('The loop ends at ', number)



    