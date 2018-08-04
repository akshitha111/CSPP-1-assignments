""" digit product """
def main():
    '''
    Read any number from the input, store it in variable int_input.
    '''
COUNT = 0
i = 1
S = int(input())
DI = 0
P = i
while S == 0:
    DI = S%10
    S = S//10
    P = P*DI
print(P)

if __name__ == "__main__":
    main()
