'''
Write a function to clean up a given string by removing the special characters and retain 
alphabets in both upper and lower case and numbers.
'''
import re
def clean_string(string):
    
    #stre = str(input())

    my_new_string = re.sub('[^ a-zA-Z0-9]', '', string)
    my_new_string = my_new_string.replace(" ","")
    return(my_new_string)


def main():
    string = input()
    print(clean_string(string))

if __name__ == '__main__':
    main()
