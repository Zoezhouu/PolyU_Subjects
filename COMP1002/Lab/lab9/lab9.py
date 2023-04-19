# exercise 9.1
infile = open("test.txt","r")
data = infile.read()
print(len(data))
print(data)
for i in range(30):
    print(data[i],ord(data[i]),end="")

# exercise 9.2
infile=open("test.txt","r")
for i in range (5):
    line = infile.readline()
    print(len(line))
    print(line[:1])

# exercise 9.3
infile = open('test.txt','r')
for line in infile.readlines():
    print(len(line))
    print(line)


# exercise 9.3.*


# exercise9.4
input_file = open("some.txt","r")
output_file = open("clone.txt","w")
content = input_file.read()
output_file.write(content)
output_file.close()


# exercise 9.4.2
infile=open('comp.txt','r')
content=infile.read()
print(content)
infile.close()
outfile=open('clone3.txt','w')
outfile.write(content)
outfile.close()



# exercise 9.5
input_file=open("some.txt","r")
output_file=open("clone2.txt","a")
content=input_file.read()
output_file.write(content)
output_file.close()



# exercise 9.6
infile=open('student.csv','r')
lines = infile.readlines()
list1=[]
for line in lines:
   items = line.split(',')
   for item in items:
       print('{0:20}'.format(item),end='')
   print()



# exercise 9.6.2
infile = open('student.csv','r')
lines=infile.readlines()
sizes = [0 for a in lines[0].split(',')]
print(sizes)

for line in lines:
    i=0
    for cell in line.split(','):
        if len(cell) > sizes[i]:
            sizes[i] = len(cell)
        i+=1

print(sizes)
size=20

for line in lines:
    items = line.split(',')
    i=0
    for item in items:
        print('{0:20}'.format(item,size[i]+2),end='')
        i+=1
    # print()
        
    

















