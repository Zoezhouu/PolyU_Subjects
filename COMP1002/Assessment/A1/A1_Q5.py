#input1: 17    output1: 10001
#input2: 80    output2: 1010000
#input3: 119   output3: 1110111
dec = int(input("Please enter a positive integer:"))
bi = []
while dec >= 0:
    r = dec % 2
    q = dec // 2
    bi = bi + [r]
    if q == 0:
        break
    dec = q
bi[::-1]
bi1 =[str(x) for x in bi]
print (''.join(bi1))