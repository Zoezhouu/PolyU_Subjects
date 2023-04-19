def mySplit(txt,sep):
    # function for splitting text into words seperately
    words = []
    wordlist=[]
    a = ''
    for ch in txt:
        if ch == ' ' or ch in sep:
            words.append(a)
            a=''
        else:
            a += ch
    
    for i in words:
        if i != '':
            wordlist.append(i)
            
    return wordlist


def a3q3():
    # read input and check output
    txt= input('Please input a paragraph: ')
    sep = [',', '?', '.','!',';']
    wordlist = mySplit(txt, sep)
    print('A list of words from your input:')
    print(wordlist)

a3q3()
