""" digit product """
def main():
    '''
    Read any number from the input, store it in variable int_input.
    '''
i = int(input())
P = 1
while i > 0:
    A = i%10
    i = i//10
    P = P * A
print(P)

if __name__ == "__main__":
    main()

