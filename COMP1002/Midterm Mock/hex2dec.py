import math
def convertDectoHex(a):
    al=list(a)
    b={'A':10,'B':11,'C':12,'D':13,'E':14,'F':15}
    multi=0
    sumof=0
    for i in range(len(a)):
        if al[i] in b.keys():
            multi=int(b[al[i]])
        else:
            multi=int(al[i])
        sumof+=multi*math.pow(16,len(a)-i-1)
    return sumof
a=input('base 16 representation:')
print('Number in base 16{}is converted to base 10 representation --{}.'.format(a,convertDectoHex(a)))
print(sumof)