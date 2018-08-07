"""
# Exercise: GCDIter
# This function takes in two numbers and returns one number.
"""
def gcditer_1(a_1, b_1):
    """ gcd """
    while a_1 != b_1:
        if a_1 > b_1-1:
            a_1 = a_1 - b_1
            return a_1
        b_1 = b_1-a_1
        return b_1
def main():
    """ gcd """
    data = input()
    data = data.split()
    print(gcditer_1(int(data[0]), int(data[1])))
if __name__ == "__main__":
    main()
