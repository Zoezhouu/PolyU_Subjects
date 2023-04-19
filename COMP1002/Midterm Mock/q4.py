# input: positive integer
# output: whether the number is a prime

n = int(input("please enter one positive number:"))
for i in range (2,n):
    if n % i == 0:
        print(n,"is not a prime.")
        break
    else:
        print(n,"is a prime.")