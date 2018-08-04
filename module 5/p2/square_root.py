'''
# Write a python program to find the square root of the given number
# using approximation method

# testcase 1
# input: 25
# output: 4.999999999999998

# testcase 2
# input: 49
# output: 6.999999999999991
'''
def main():
    '''
    # Write a python program to find the square root of the given number
    # using approximation method

    # testcase 1
    # input: 25
    # output: 4.999999999999998

    # testcase 2
    # input: 49
    # output: 6.999999999999991
    '''

A_I = int(input())
E_B = 0.01
S_C = 0.1
G_Y = 0.0
while abs(G_Y **2-A_I) >= E_B:
    if G_Y <= A_I:
        G_Y += S_C
    else:
        break
if abs(G_Y**2 - A_I) >= E_B:
    print("failed")
else:
    print(str(G_Y))
    # epsilon and step are initialized
    # don't change these values
    # your code starts here

if __name__ == "__main__":
    main()
