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
E_N = 0.01
G_S = A_I/2.0
while abs(G_S*G_S - A_I) >= E_N:
    G_S = G_S - (((G_S**2) - A_I)/(2*G_S))
    print(str(G_S))

if __name__ == "__main__":
    main()
