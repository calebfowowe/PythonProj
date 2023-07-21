x = float(input("Enter the value of x: "))
y = float(input("Enter the value of y: "))
z = x/y
p = z**2
print(f"x divided by y is {z:.2f}")
print("the results above squared is:", round(p,2))

def hello(to):
    print("hello,", to)

name = input("What is your name:")
hello(name)
