"""
# Exercise: GCDRecr
# This function takes in two numbers and returns one number.
"""


def gcdrecur_1(a_1, b_1):
    '''
    gcd
    '''
    r_1 = 0
    if a_1%b_1 == 0:
        return b_1
    r_1 = a_1%b_1
    a_1 = b_1
    b_1 = r_1
    return gcdrecur_1(a_1, b_1)
def main():
    """ gcd """
    data = input()
    data = data.split()
    print(gcdrecur_1(int(data[0]), int(data[1])))

if __name__ == "__main__":
    main()
