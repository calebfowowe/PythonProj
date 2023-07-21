"""
#Exercise 9 Fibonacci Series
fb_1 = 1
fb_2 = 1
num = int(input("Enter the number of fibonacci series you wish to print: "))
print(fb_1, fb_2, sep=",", end=",")
for i in range(2,num):
    fb_3 = fb_1 + fb_2
    print(fb_3, end=",")
    fb_1 = fb_2
    fb_2 = fb_3
print()

#Exercise 10
height = eval(input('Enter the preferred height:'))
width = eval(input('Enter the preferred width:'))
for i in range (height):
    print('*' * width)
    
#Exercise 11
height = eval(input('Enter the preferred height:'))
width = eval(input('Enter the preferred width:'))
first_row= '*' * width
print(first_row)
for i in range (2,height):
    i = ('*') + (' '* (width-2)) + ('*')
    print(i)
print(first_row)

#Exerice 12
height = eval(input('Enter the height of the triangle:'))
for i in range (height):
    print('*' * (i+1))
"""
#Exercise14
height = int(input('Enter the preferred height:'))
h = int(height/2)
for i in range (h):
    w = h - i
    z = (' '*(w)) + ('*'*((i+i)+1)) + (' '*(w)) 
    print(z)
for i in range (h,-1,-1):
    w = h - i
    z = (' '*(w)) + ('*'*((i+i)+1)) + (' '*(w)) 
    print(z)