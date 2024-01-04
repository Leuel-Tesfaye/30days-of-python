# conditional execution : a block of one or more statements will be executed if a certain expression is true. 
# repetitive execution : a block of one or more statements will be repetitively will be executed as long as a certain expression is true.

#! if condition 
# if is used to check if a condition is true and to execute the block code.
a = 3 
if a > 0 : 
    print('A is a positive number')

#! If Else
# If condition is true the first block will be executed, if not the else condition will run.

number = int(input('please enter a number :'))
if number > 0:
    print('The number you entered is a positive number !')
else :
    print('The number you entered is a negative number')

#! If Elif Else
    # We make decisions not by checking one or two conditions but multiple conditions. 
age = int(input('please Enter your age: '))
if age > 18 :
    print('The person is legal to vote')
elif age > 120 :
    print('This kind of age is not supported')
else :
    print('The person is not legal to vote')

#! nested conditions 
num = int(input('please Enter number :'))
if num > 0:
   if num % 2 == 0 :
      print('The number you entered is an even number !')
   else :
       print('The number you entered is an odd number !')
elif num < 0 :
    print('The number you enter is a negative number')
else :
    print('Please try again !')

#! If Condition (and , or) Logical Operators
user = input(' Enter username :')
access_level = int(input('Enter your access level: '))

if user == 'leuel' and access_level >= 5: # if and is substituted by "or" the first condition will be executed if one of the conditions full fill . 
    print('Access granted')
else :
    print('Access denied ')


