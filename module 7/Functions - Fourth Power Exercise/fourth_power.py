""" fourth power """
def square():
    '''
    x: int or float.
    '''
    # Your code here
def fourth_power(x_1):
    '''
    x: int or float.
    '''
    # Your code here
    return x_1**4
def main():
    """ fourth_power """
    data = input()
    data = float(data)
    temp = str(data).split('.')
    if temp[1] == '0':
        print(fourth_power(int(float(str(data)))))
    else:
        print(fourth_power(data))

if __name__ == "__main__":
    main()
