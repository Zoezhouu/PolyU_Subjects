# exercise 4.1
sum = 0
current = 1
n = int (input("Enter a value:"))
while current <= n:
    sum = sum + current
    current = current + 1

# exercise 4.2
sum = 0
current = 1
n = int (input("Enter a value:"))
while current < n:
    sum = sum + current
    current = current + 1

# input error checking
# exercise 4.3
# Display program welcome
print("This program converts temperatures (Fahrenheit/Celsius)")
print("Enter (F) to convert Fahrenheit to Celsius")
print("Enter (C) to convert Celsius to Fahrenheit")

# Get temperature to convert
f_or_c = input("Please enter selection: ")

while f_or_c != "F" and f_or_c != "C":
    f_or_c = input("Please enter selection again: ")
    temp = int(input("Enter temperature to convert: "))

# Get input temperature
temp = input("Enter temperature: ")
while True:
    try:
        temp = eval(temp)
    except:
        temp = input("Enter temperature again: ")
    break

if f_or_c == "C":
    #C2F
    print ("The temperature is", 9/5 * temp + 32,"degrees Fahrenheit")
else:
    #F2C
    print ("The temperature is", (temp-32)*5/9,"degrees Celsius")



# while <condition>:
#     <body>
#     *condition is a boolean expression 

# exercise 4.4
templist = eval(input("Enter temperatures: "))
for temp in templist:
    if f_or_c == "C":
        #C2F
        print ("The temperature is", 9/5 * temp + 32,"degrees Fahrenheit")
    else:
        #F2C
        print ("The temperature is", (temp-32)*5/9,"degrees Celsius")

# exercise 4.5
# error checking 

# exericse 4.6
symbol = input("Please enter a symbol: ")
line = eval(input("Please enter a positive position of the symbol on the first line: "))
space = line+1
i = 0

while i <= line:
    space -= 1
    i+=1
    print(space * " ", (2*i-1) * symbol)
