# exercise 3.1
x,y,z = 1,2,3
print(x==y)     # False
print(x>y)      # False
print(x+y+z>10) # False
# print(False = True)     # SyntaxError: cannot assign to False
print(False == True)    # False
print(False>True)       # False
print(True>False)       # True

# exercise 3.2
x,y,z = "Benjamin","Ben","ben"
print(x>y)      # True
print(y>z)      # False
print(y+z>x)    # False
print("abc">"123")  # True
print("abc">">>>")  # True

# Try
print(10 in [10,20,30,40])  # True
print(10 not in [10,20,30,40])  # False
print("blue" in ["red","yellow","black"])   # False
print("blue" not in ["red","yellow","black"])   # True
print("o" in "peter paul and mary")     # False

# exercise 3.3
print(True and False)   # False
print(True or False)    # True
print(not(True) and False)  # False
print(not (True and False)) # True
print((10>0) and (10>2))    # True
print((10<0) or(10>2))      # True
print(not(10<0) or(10>2))   # True
print(not(10<0 or 10>2))    # False

# exercise 3.4
print(True or False and True and True)  # True
print(True or not False and True and not True)  # True
print(((True or not False) and True) and not True)  # False

# exercise 3.5
iq=eval(input("Please enter your IQ:"))
if iq>=130:
    print("Your IQ is very superior.")
elif 120<=iq<=129:
    print("Your IQ is superior.")
elif 110<=iq<=119:
    print("Your IQ is high average.")
elif 90<=iq<=109:
    print("Your IQ is average.")
elif 80<=iq<=89:
    print("Your IQ is low average.")
elif 70<=iq<=79:
    print("Your IQ is borderline.")
else:
    print("Your IQ is extremely low.")



# exercise 3.6
# pseudocode:
# Input: three numbers a,b,c
# Output: numbers in descending order
# set a,b,c as three number
# if a>b
#    if a>c
#        if c>b, then print a,c,b
#        else(c<b), then print a,b,c
#    else (a<c), then print c,a,b
#  else(a<b)
#    if a>c, then print b,a,c
#    else(a<c),
#        if c>b, then print c,b,a
#        else(c<b), then print b,c,a


a,b,c=eval(input("Please enter three number with comma between numbers:"))
if a>b:
    if a>c:
        if c>b:
            print (a,c,b)
        else:
            print (a,b,c)
    else:
        print (c,a,b)
else:
    if a>c:
        print (b,a,c)
    else:
        if c>b:
            print (c,b,a)
        else:
            print (b,c,a)


# exercise 3.7
i=2
while i<10:
    print (i)
    i=i+2

# exercise 3.8
i=0
while i<=9:
    print(i)
# no ends


#interactive loop
moredata = "yes"
sum = 0.0
count = 0
while moredata [0] == 'y':
    x = int (input("Enter a number >>"))
    sum= sum + x
    count = count + 1
    moredata = input("Do you have more numbers (yes or no)?")
print("\nThe average of the numbers is", sum / count)