def main():
    string= str(input("Input a string:"))
    location = eval(input("Input a zero-base location in a string to be changed:"))
    b = str(input("Input a character to be updated in that location:"))
    s1 = list(string)
    s1[location] = b
    s = ''.join(s1)
    strs = changeString(str(s))
    print ("The string updated:",strs)
    
def changeString(strs):
    strs=''