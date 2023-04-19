#String data type
str1="Hello"
str2='spam'
print(str1,str2)

# Hello spam
type(str1)  # <class 'str'>
type(str2)  # <class 'str'>

# exercise 5.1
# Indexing
str="Hello World!"
str[0]  # 'H'
str[5]  # ' '
str[11] # '!'
str[12] # IndexError: string index out of range
#<str>[<expr>]

# exercise 5.2
str='Hello World!'
str[-1]     # '!'
str[-7]     # ' '
str[-12]    # 'H'
str[-13]    # IndexError: string index out of range

# exercise 5.3
#   slicing
#   <string>[<start>:<end>]
str="Hello World!"
str[0:3]    # 'Hel'
str[5:9]    # ' Wor'
str[5:]     # ' World!'
str[;]      # SyntaxError: invalid syntax

# Negative indices
str[-1:-5]  # ''
str[-5:-1]  # 'orld'


# exercise 5.4
# concatenation: +
# repetition: *
# Length: len(<string>)
str1="sausage"
str2="egg"
str1+"and"+str2         # 'sausageandegg'
3*str1                  # 'sausagesausagesausage'
(3*str1)+(2*str2)       # 'sausagesausagesausageeggegg'
len(str1+"and"+str2)    # 13

# exercise 5.5
# Iteration through characters(for <var> in <string>)
for ch in "Sausage":
    print(ch,end=" ")
# S a u s a g e


# exercise 5.6
firstname=input("Please enter your first name:")
lastname=input("Please enter your last name:")
print("Your username is",firstname[0]+lastname[0:6])


# List
myList = [1,2,3,4]
myGrades=["A+","A","B+","B"]
myMenu=["Sausage","egg","bread","potato"]
myMix = [1,"Spam",4,"U"]

# exercise 5.7
# concatenation: +
# repetition: *
# indexing: <list>[]
# slicing: <list>[:]
# length: len(<list>)
# iteration through list items: for <var> in <list>
myList1=[1,2,3,4]
myList2=[5,6,7,8]
myList1+myList2     # [1, 2, 3, 4, 5, 6, 7, 8]
myList1[0]          # 1
myList1[2:4]        # [3, 4]
len(myList1)        # 4

# exercise 5.8
myGrades=["A+","A","B+","B"]
myName = "Dennis Liu"
myGrades[0]="C"
myName[0]="C"       # TypeError: 'str' object does not support item assignment
print (myGrades)    # ['C', 'A', 'B+', 'B']


# Native data types
# difference with the object data types
# each object contains data and each object also has methods operated in the data

# exercise 5.9
student = "first_name last_names students_ID"
student.lower()         # 'first_name last_names students_id'
student.upper()         # 'FIRST_NAME LAST_NAMES STUDENTS_ID'
student.capitalize()    # 'First_name last_names students_id'
student.split()         # ['first_name', 'last_names', 'students_ID']
student.title()         # 'First_Name Last_Names Students_Id'

# string methods
# str.capitalize()
# str.casefold()
# str.center (width[, fillchar)
# str.count (sub[, start[,end]])
# str.title()
# str.translate (map)
# str.upper()
# str.zfill (width)

# lists methods
# list.append(obj)
# list.count(obj)
# list.extend(seq)
# list.index(obj)
# list.remove(obj)
# list.reverse()

# turn a list into a string
# s.join(list) - concatenate list into a string, using s as a separetor
# s.join(list) - concatenate str into a string, using s as a seperator

# exericse 5.10
list=["A","B","C","D"]
"".join(list)   # 'ABCD'


# Notes:
# string 
# data type: quotation marks("") or apostrophe ('')
# indexing a string: <string>[<expr>]
# slicing a string: <string>[<start>:<end>]
# Negative indices
# concatenation: +
# repetition: *
# Length: len(<string>)
# iteration through characters: for <var> in <string>

# list
# data type: a sequence of arbitrary objects
# concatenation: +
# repetition: *
# indexing: <list>[]
# slicing: <list>[:]
# length: len(<list>)
# iteration through list items: for <var> in <list>