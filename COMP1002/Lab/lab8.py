# 8.1
hongva=100
dennis=200
print("hongva has ${0:0.2f} and Dennis has ${1:0.2f}".format(hongva,dennis))
print("hongva has ${1:0.2f} and Dennis has ${0:0.2f}".format(hongva,dennis))

# 8.2
dennis= 100
print("Dennis has ${0:0.2f}".format(dennis))
print("Dennis has ${0:1.2f}".format(dennis))
print("Dennis has ${0:5.2f}".format(dennis))
print("Dennis has ${0:10.2f}".format(dennis))

# 8.3
import math
print("The value of pi is {0:0.4f}".format(math.pi))
print("The value of pi is {0:0.20f}".format(math.pi))
print("The value of pi is {0:0.20}".format(math.pi))

# 8.4
print("{0:>10}".format("Dennis"), "|", "Liu",sep='')
print("{0:10}".format("Dennis"), "|", "Liu",sep='')
print("{0:^10}".format("Dennis"), "|", "Liu",sep='')

# 8.5
dict={'a':1,'apple':1,'b':1,'boy':1,'c':1,'cat':1,'d':1,'dog':1,'for':4}
print("{0:^10}".format("Key"), "|", "{0:^10}".format("Count"),sep='')
print('-'*19)

for keys, values in dict.items():
    print("{0:^9}".format(keys), "|", "{0:^9}".format(values),sep='')


# 8.6
#set allows tuple, string and elements does not allowed list.
len(set)
# set.add(element)
set.remove


# 8.7
a = {10,20,30,40,30,40}
print(a)    # {40, 10, 20, 30}
print(40 in a)  # True
print(1 in a)   # False
a.add(50)
print(a)    # {40, 10, 50, 20, 30}
a.remove(10)
print(a)    # {40, 50, 20, 30}
b={10,20,30}
print(a|b)  # {50, 20, 40, 10, 30}
print(a.union(b))   # {50, 20, 40, 10, 30}
print(a&b)      # {20, 30}
print(a-b)      # {40, 50}
print(a^b)      # {40, 10, 50}
print(len(a))   # 4

