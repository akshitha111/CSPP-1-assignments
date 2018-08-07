"""
# Exercise: Assignment-2
# This function takes in one number and returns one number.
"""
def sumofdigits(n_1):
    """ sum """
    while n_1 > 0:
        r_1 = n_1%10
        return r_1+sumofdigits(n_1//10)
    return 0
def main():
    """ sum """
    a_1 = input()
    print(sumofdigits(int(a_1)))
if __name__ == "__main__":
    main()
