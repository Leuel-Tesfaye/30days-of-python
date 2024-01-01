
# Write a script that prompts the user to enter base and height of the triangle and calculate an area of this triangle (area = 0.5 x b x h).
base = int(input('please Enter base: '))
height = int(input('please Enter height: '))

area_of_triangle = 0.5 * base * height
print ('The area of a triangle is :' , area_of_triangle)

# ? Get radius of a circle using prompt.  circumference (c = 2 x pi x r) where pi = 3.14.
# r stands for radius 
# c stands for circumference

r = int(input('please Enter the radius of a circle :'))
pi = 3.14
c = 2 * pi * r

print('The circumference of the circle is :' , c)

# !Find the length of 'python' and 'dragon' and make a falsy comparison statement.
print (len('python') != len('dragon'))

#? Use and operator to check if 'on' is found in both 'python' and 'dragon'
print('on' in 'python' and 'on' in 'dragon')


