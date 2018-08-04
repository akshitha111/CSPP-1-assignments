'''
Replace all the special characters(!, @, #, $, %, ^, &, *) in a given string with a space.
example : ab!@#cd is the input, the output is ab   cd
Output has three spaces, which are to be replaced with these special characters
'''
def main():
    '''
    Read string from the input, store it in variable str_input.
    '''
S = input()
S_O = ""
for char in S:
    if char == '!' or char == '@' or char == '#' or char == '$' or char == '%' or char == '^' or char == '&' or char == '*':
        S_O = S_O + " "
    else:
        S_O = S_O + char
print(S_O)

if __name__ == "__main__":
    main()
