# Get user input using input(“Enter your age: ”). If user is 18 or older, give feedback: You are old enough to drive. If below 18 give feedback to wait for the missing amount of years. 

age = int(input('Enter your age : '))

if age >= 18 :
    print('you are old enough to drive !')
else : 
    print('you have to wait', 18 - age , 'more years to be old enough to drive !' )


