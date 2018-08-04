""" digit product """
def main():
    '''
    Read any number from the input, store it in variable int_input.
    '''
S = int(input())
P = 1
while S > 0:
    A = S%10
    S = S//10
    P = P * A
print(P)

if __name__ == "__main__":
    main()

