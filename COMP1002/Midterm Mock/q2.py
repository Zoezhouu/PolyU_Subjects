# input: positive integer, x
# output: binary number

x = int(input("Please enter a positive integer, x:"))
bi = []
while x >= 0:
    r = x % 2
    q = x // 2
    bi = bi + [r]
    if q == 0:
        break
    x = q
bi[::-1]
bi1 =[str(i) for i in bi]
print (''.join(bi1))

