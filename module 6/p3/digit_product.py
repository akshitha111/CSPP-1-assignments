""" digit product """
def main():
    '''
    Read any number from the input, store it in variable int_input.
    '''
S = int(input())
i = 1
for i in S:
    A = S%10
    S = S/10
    S = S%10
    A = A * i
print(A)

if __name__ == "__main__":
    main()
