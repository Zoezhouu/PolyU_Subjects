import math
# exercise 2.1
# Is 3.3333333333e3 or 3.33e33 larger?

# exercise 2.2
print(round(0.45,1))
print(round(1.45,1))
print(round(2.45,1))
print(round(3.45,1))
print(round(4.45,1))
print(round(5.45,1))
print(round(6.45,1))
print(round(7.45,1))
print(round(8.45,1))
print(round(9.45,1))

print(math.ceil(5.45))
print(math.floor(5.45))
print(math.ceil(-5.45))
print(math.floor(-5.45))

print(int(5.45))
print(int(-5.45))
print(float(5))


# exercise 2.3
print('') # two single quotes without space
print("") # two double quotes without space
print(" ' ")
print(' " ')
# print("') # double quote + single quote
ord ('') # two single quotes without space
ord (' ') # space inside
ord ("") # two double quotes without space
ord (" ") # space inside

# exercise 2.4
print("1\t2\t3")
print("1\b2\n3")
print("\"")
# print("\\"")
print("\\")
# print("\")
print("\u5927")

# exercise 2.5
x = eval(input("Input an integer:"))
y = eval(input("Input another integer:"))
print(x,y)

# exercise 2.6
x, y = eval(input("Input two integers:"))
print(x,y)

# exercise 2.7
print(2**3**4)
print(8+4-2)
print(8-4-2)
print(8*4/3)
print(8/4/2)

# exercise 2.8
x = 10
print(type(x))
x = 10.0
print(type(x))

# exercise 2.9
print(type(6+3))
print(type(6.0+3.0))
print(type(6.0+3))
print(type(6.00+3.00))
print(type(6*3))
print(type(6.0*3.0))
print(type(6.0*3))
print(type(6/3))
print(type(6.0/3.0))
print(type(6.0/3))

# exercise 2.10
print(int(11.1))
print(int("11"))
print(int("11.1"))
print(float(11))
print(float("11"))
print(float("11.1"))
print(float("1.111111111111111"))