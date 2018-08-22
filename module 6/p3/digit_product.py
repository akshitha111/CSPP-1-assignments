""" digit product """
def main():
    '''
    Read any number from the input, store it in variable int_input.
    '''
    s_inp = int(input())
    product = 1
    temp = 0
    if s_inp < 0:
        temp = 1
        s_inp = -s_inp
    if s_inp == 0:
        product = 0
    while s_inp != 0:
        rem = s_inp%10
        s_inp = s_inp//10
        product = product * rem
    # return -product if t==1 else product
    if temp == 1:
        print(-product)
    else:
        print(product)

if __name__ == "__main__":
    main()
