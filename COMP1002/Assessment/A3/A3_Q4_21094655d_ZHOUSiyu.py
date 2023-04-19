def wordFeq(word_list):
    # this function is to sort word in decreasing order of their frequency
    count = dict()
    for i in word_list:
        count[i] = count.get(i, 0) + 1 # calculare the frequency of each word
    word_list = sorted(set(word_list), key = lambda i:(-count[i], i)) # sort the word by frequency
    sort_list = []
    for i in word_list:
        sort_list.append([i, count[i]])
    return sort_list

def mySplit(data):
    # this function is to return a list of words from file, words will be saved by removing redundant characters
    word_list = list()
    for text in data.split(): #split words
        i = []
        for ch in text:
            if ch.isalnum(): #check if the string is composed of letters and numbers
                i.append(ch) 
        if len(i) > 0:
            word_list.append(''.join(i)) 
    return word_list

def a3q4():
    # this function is read input and check output
    file = open('a3q4.txt')
    data = file.read()
    word_list = mySplit(data)
    sort_list = wordFeq(word_list)
    print(f'{"Words":^20}|{"Frequency":^20}')
    print('-'*40)
    for word, freq in sort_list:
        print(f'{word:^20}|{freq:^20}')

a3q4()