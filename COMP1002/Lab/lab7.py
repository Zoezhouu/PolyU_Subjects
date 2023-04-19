myList = (1,2,3,4)
print(myList)   # (1, 2, 3, 4)
myList1 = [1,2,3,4]
print(myList[0])    # 1
# print(myList[0]=10) # TypeError: 'tuple' object does not support item assignment
# print(myList1[0]=10)
print(myList1)  # [10, 2, 3, 4]

myGrades=("A+","A","B+","B")
myMenu=("Sausage","egg","bread","potato")
myMix=(1,"Spam",4,"U")
myEmptiness=()
mySingleton=(1,)


# exercise 7.1
x=(1,2,3,4)
print(x)    # (1, 2, 3, 4)
print(id(x))    # 2246678292976
print(hex(id(x)))   # '0x20b187629f0'
# print(x[0]=10)      # TypeError: 'tuple' object does not support item assignment
y=(9)
z=(9,)
print(type(y))  # <class 'int'>
print(type(z))  # <class 'tuple'>

# exercise 7.2
# append()
# insert()
# sort()
# reserve()
# del()

#exercise 7.3
nickname=dict()
print(nickname) # {}
nickname={"Mickey":"Mickey Mouse in Disney","Minnie":"Minnie Mouse in Disney"}
print(nickname) # {'Mickey': 'Mickey Mouse in Disney', 'Minnie': 'Minnie Mouse in Disney'}
nickname["Woody"] = "Woody in Toy Story"
print(nickname)

# "Mickey" is the key
# "Mickey Mouse in Disney" is the value

# exercise 7.4
dictC={"a":1,"b":{"aa":11,"bb":22}}
print(dictC["b"])   # {'aa': 11, 'bb': 22}
print(type(dictC["b"]))     # <class 'dict'>
print(dictC["b"]["aa"])     # 11
print(dictC["b"]["bb"])     # 22

# exercise 7.5
dictD={"a":1,"b":{"aa":11,"bb":22}}
print(len(dictD))

# exercise 7.7
str = "a for apple b for boy c for cat d for dog"
words = str.split()
dict = {}
for i in words:
    dict[i] = words.count(i)
print(dict)
for keys, values in dict.items():
    print(keys, values)