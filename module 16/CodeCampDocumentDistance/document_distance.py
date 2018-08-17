'''
    Document Distance - A detailed description is given in the PDF
'''

def similarity(dict1, dict2):
    '''
        Compute the document distance as given in the PDF
    '''
    dict1 = ""
    dict2 = ""
    word_frequencies = {}
    for i,v in word_frequencies:
        word_frequencies.i = words
        word_frequencies.v[0] = wordcount(dict1)
        word_frequencies.v[1] = wordcount(dict2)
    word_list = word_list.lower()
    document_distance = 0
    count = 0
    if i in dict1 and i in dict2:
        count = count+i
        return count
    return 0




def load_stopwords(filename):
    '''
        loads stop words from a file and returns a dictionary
    '''
    stopwords = {}
    with open(filename, 'r') as filename:
        for line in filename:
            stopwords[line.strip()] = 0
    return stopwords

def main():
    '''
        take two inputs and call the similarity function
    '''
    input1 = input()
    input2 = input()

    print(similarity(input1, input2))

if __name__ == '__main__':
    main()
