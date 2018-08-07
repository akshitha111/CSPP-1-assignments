""" # Exercise: PowerIter
# This function takes in two numbers and returns one number.
"""


def iterPower_1(base, exp):
    '''
    base
    '''
    # Your code here
    b_1 = 1
    for i in range(1, exp+1):
        b_1 = base*b_1
    return b_1
def main():
    """ base """

    data = input()
    data = data.split()
    print(iterPower_1(float(data[0]), int(data[1])))
if __name__ == "__main__":
    main()
