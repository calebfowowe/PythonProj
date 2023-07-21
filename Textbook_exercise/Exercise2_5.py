#Fibonacci Series
fb_1 = 1
fb_2 = 1
num = int(input("Enter the number of fibonacci series you wish to print: "))
print(fb_1, fb_2, sep=",", end=",")
for i in range(2,num):
    fb_3 = fb_1 + fb_2
    print(fb_3, end=",")
    fb_1 = fb_2
    fb_2 = fb_3
    