def partA():
    a = str(input("Please enter a list of different numbers seperated by \',\' :"))
    b = ""
    bList=[]
    for c in a:
        if c == ",":
            bList.append(b)
            b = ""
        else:
            b = b + c
    bList.append(b)
    map1=min(list(bList))
    print("The minimum number is",str(map1["minvalue"]))
    print("Its location is", str(map1["location"]))

def min(list1):
    location = 0
    minvalue = 0
    for i,c in enumerate(list1):
        if i == 0:
            minvalue = int(c)
        if int(c) < minvalue:
            minvalue = int(c)
            location = i
    return {"minvalue":minvalue,"location":location}




def partB():
    a = input("Please enter a list of different numbers separated by \',\': ")
    b = ""
    bList = []
    for i in a:
        if i == ",":
            bList.append(b)
            b = ""
        else:
            b = b + i
    bList.append(b)
    listx=sorting(bList)
    print("A list of sorting values in ascending order:", str(listx))

def sorting(list1):
    list2=[]
    while len(list1) > 0:
        m = min(list1)
        list1.remove(m)
        list2.append(m)
    list1=list2



