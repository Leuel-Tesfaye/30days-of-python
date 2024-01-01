
# Text is a string datatype. Any data in single , double or triple quote are strings. 
greeting = 'hello python world !'
print(greeting)

# multiline string is created using triple quote.
multiline_string = '''I am a teacher and enjoy teaching.
I didn't find anything as rewarding as empowering people.
That is why I created 30 days of python.'''
print(multiline_string)

#? slicing python strings
language = 'python'
first_three = language[0:3]
print(first_three)
 
#? reversing a string 
print(greeting [:: -1])

# ? string methods 
#? capitalize
challenge = 'Thirty days of python'
print(challenge.capitalize())

#? count() : returns occurrences of substring in string

print(challenge.count('y'))
print(challenge.count('i'))

#? join() : returns a concatenated string
web_tech = ['html', 'css', 'js', 'python', 'react']
result = ' '.join(web_tech)
print(result)

#? replace () : replaces substring with a given string 
challenges = 'Thirty days of javascript'
print(challenge.replace('javascript', 'python'))



