import math

# def avg(n1,n2,n3):
#     print((n1+n2+n3)/3)
# def avgR(n1,n2,n3):
#     print((n1+n2+n3)/3)
#     return(n1+n2+n3)/3
# def sumDiff (x,y):
#     sum = x + y
#     diff = x - y
#     return sum, diff

# exercise 6.1
def printNumbers (n1, n2,n3):
    print(n1, n2, n3)

m1, m2, m3 = 10, 20, 30
printNumbers(m1, m2, m3)
printNumbers(n2=m2, n1=m3, n3=m1)


printNumbers    # <function printNumbers at 0x0000029DF65955E0>
m1,m2,m3=10,20,30
print(m1)       # 10
print(m2)       # 20
print(m3)       # 30
printNumbers(m1,m2,m3)  # 10 20 30
printNumbers(n2=m2,n1=m3,n3=m1) # 30 20 10


# default
# print("The default print() parameters.")
# print("The default print() parameters.", end=" n")
# print("The default print() parameters.", sep =" ")
# print("The default print() parameters.", end=" n", sep =" ")
# print("The default print() parameters.", sep =" ", end=" n")



# exercise 6.2
def addInterest (balance,rate):
    newBalance = balance * (1 +rate)
    balance = newBalance
def test():
    amount = 1000
    rate = 0.05
    addInterest(amount,rate)
    print("My current balance is: ", amount)
test()



def addInterest (balance,rate):
    balance = balance * (1 + rate)
def test():
    amount = 1000
    rate = 0.05
    addInterest(amount,rate)
    print("My current balance is: ", amount)
test()

a=10
print(id(a))    # 2513785416272
print(hex(id(a)))   # '0x24949496a50'
b=a
print(b)    # 10
print(id(b))    # 2513785416272
a=20    
print(a)    # 20
print(b)    # 10
print(id(a))    # 2513785416592
print(id(b))    # 2513785416272


#example
def addInterest (balances,rate):
    for i in range(len(balances)):
        balances[i] = balances[i] * (1+rate)

def test():
    amounts = [1000, 2150, 800, 3275]
    rate = 0.05
    addInterest(amounts,rate)
    print(amounts)

test()


a=[10,2,3,4]
b=[10,2,3,4]
print(a==b) # True
print(a is b)   # False
print(b is a)   # False
print(id(a))    # 2513825401920
print(id(b))    # 2513825295424
b=[100,200,300,400]
print(b)        # [100, 200, 300, 400]
print(a)        # [10, 2, 3, 4]
print(id([100,200,300,400]))    # 2513825360896


# exercise 6.4
def funList (aList):
    aList.append(1)
    aList = [2,3]

L1 = [0]
funList(L1)
print(L1)


# exercise 6.5

def funA():
    print(x)
def funB():
    # x is a local variable
    x = 2
    print(x)

# x is a global variable
x = 10
funA()
funB()
print(x)



# exercise 6.6
x = 1
def fun():
    x = x + 1
    print(x, "x inside fun()")
print(x, "x outside fun()")
fun()


# exercise 6.7
# >>> help(math)
# >>> dir(math)
print(math.__doc__)



# exercise 6.8
def sum(a,b):
    '''Takes in 2 number a and b, returns a + b'''
    # this is a docstring
    return a + b


def main():
    a,b = eval(input("Please enter 2 numbers"))
    print(sum(a, b))
    print(sum.__doc__)
main()






