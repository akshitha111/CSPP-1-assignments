""" digit product """
def main():
    '''
    Read any number from the input, store it in variable int_input.
    '''
    S = int(input())
    P = 1
    t = 0
    if S < 0:
        t = 1
        S = -S
    while S > 0:
        A = S%10
        S = S//10
        P = P * A
    return -P if t==1 else P
# if t = 1:
#   P = -P
# else: 
# print(P)

if __name__ == "__main__":
    main()
