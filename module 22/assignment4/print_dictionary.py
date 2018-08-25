'''
Write a function to print a dictionary with the keys in sorted order along with the
frequency of each word. Format of the printing should be one key per line and separate
the key and frequency with a SPACE - SPACE.
'''

def print_dictionary(dictionary):
    with open('~/Desktop/file') as f:
    	words = f.read()
        wordfreq = {}
    for word in words.replace(',', ' ').split():
        wordfreq[word] = wordfreq.setdefault(word, 0) + 1
print wordfreq

def main():
    dictionary = eval(input())
    print_dictionary(dictionary)

if __name__ == '__main__':
    main()
