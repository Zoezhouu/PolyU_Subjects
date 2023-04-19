L = []
print("If you want to stop entering number, just type '-1'")
while True:
    x =eval (input("Please enter a number:"))
    if x !=-1:
        L = L + [x]
    else:
        break
print("The maximum numbers is",max(L))
print("Its input sequence number is", L.index(max(L))+1)