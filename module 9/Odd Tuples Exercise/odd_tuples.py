""" odd """
#Exercise : Odd Tuples
def oddtuples_1(a_1tup):
    '''
    aTup: a tuple
    returns: tuple, every other element of aTup.
    '''
    l_1 = len(a_1tup)
    a_1 = ()
    for i in range(0, l_1):
        if i%2 == 0:
            a_1 = a_1+(a_1tup[i],)
    return a_1
def main():
    """ odd """
    data = input()
    data = data.split()
    a_1tup = ()
    for j in range(len(data)):
        a_1tup += ((data[j]),)
    print(oddtuples_1(a_1tup))
if __name__ == "__main__":
    main()
