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
    '''

N_A = int(input())
E_B = 0.01
L_W = 0.0
H_I = N_A
M_I = (L_W + H_I)/2.0
while abs(M_I**2-N_A) >= E_B:
    if M_I**2 < N_A:
        L_W = M_I
    else:
        H_I = M_I
    M_I = (L_W +H_I)/2.0
print(M_I)
    # epsilon and step are initialized
    # don't change these values
        # your code starts here

if __name__ == "__main__":
    main()
