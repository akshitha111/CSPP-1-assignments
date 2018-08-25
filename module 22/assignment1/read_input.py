'''
Write a python program to read multiple lines of text input and store the input into a string.
'''

def main():
    """ read input """
    s_1 = int(input())
    #print(s)
    for line in range(s_1):
        line = str(input())
        print(line)

if __name__ == '__main__':
    main()
