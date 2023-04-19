x=eval(input("Please enter the a number for the levels:"))
for i in range(x):
    for j in range(0,i):
        print("+",end="")

    for j in range(i,2*x-i):
        print("o",end="")

    for j in range(2*x-i,2*x):
        print("-",end="")

    print("")

print("+"*x+"-"*x)