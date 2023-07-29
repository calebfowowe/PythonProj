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

#Exercise 18
c = eval(input("Enter the amount of change less then 1 dollar that you are to collect, between 0 - 99cents: "))
print(c//25, "quarters",sep="", end=", ")
c = c%25
print (c//10, "dimes",sep="", end=", ")
c = c%10
print(c//5, "nickels",sep="", end=", ")
c = c%5
print (c//1, "pennies",sep="", end=".")
c = c%1
"""
from math import *
count_nsqr = 0
count_ncub = 0
count_nfif = 0
for i in range (1,1001):
    #print(i)
    num_1a = sqrt(i)
    num_1b = i//num_1a
    num_1c = i**(1/3)
    #print('1c', num_1c)
    num_1d = i//num_1c
    #print('1d', num_1d)
    num_1e = i**(1/5)
    num_1f = i//num_1e
    if num_1b%num_1a != 0:
        #print("division_a", num_1a%num_1b)
        count_nsqr = count_nsqr + 1
    if round(num_1d%num_1c,4) != 0:
        #print(i, "division_b", num_1d%num_1c)
        count_ncub = count_ncub + 1
    if round(num_1f%num_1e,4) != 0:
        #print(i, "division_c", num_1f%num_1e)
        count_nfif = count_nfif + 1
        
print(f"There are {count_nsqr:,}non-perfect squares between 1 and 1000", sep='')
print(f"There are {count_ncub:,}non-perfect cubes between 1 and 1000", sep='')
print(f"There are {count_nfif:,}non-perfect fifths between 1 and 1000", sep='')