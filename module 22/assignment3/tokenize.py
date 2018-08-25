'''
Write a function to tokenize a given string and return a dictionary with the frequency of
each word
'''
#import re
def tokenize(string):
    def word_count(string):
        my_string = string.lower().split()
        my_dict = {}
        for item in my_string:
            my_dict[item] = item.count(item)
        print(my_dict)

        print(word_count(input()))

    
         
def main():
    num = int(input())
    input1 = ""
    for _ in range(num):
        input1 += input()
    return tokenize('')
if __name__ == '__main__':
    main()
