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
            if item in my_dict:
                my_dict[item] += 1
            else:
                my_dict[item] = 1
        print(my_dict)

    
         
def main():
    num = int(input())
    input1 = ""
    for _ in range(num):
        input1 += input()
    return (tokenize(''))
if __name__ == '__main__':
    main()
