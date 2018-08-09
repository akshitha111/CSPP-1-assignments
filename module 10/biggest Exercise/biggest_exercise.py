#Exercise : Biggest Exercise
#Write a procedure, called biggest, which returns the key corresponding to the entry with the largest number of values associated with it. If there is more than one such entry, return any one of the matching keys.


def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    # Your Code Here
    # values = aDict.values()
    # best = max(values)
    # print(best)
    # words = []
    best=0
    for k in aDict:
        # print(aDict[k])
        tempLen = len(aDict[k])
        if(tempLen>best):
            best=tempLen

    words=[]
    for x in aDict:
        tempLen = len(aDict[x])
        if(tempLen == best):
            words.append(x)
    #     if aDict[k] == best:
    #         words.append
    #         (k)
    return (words)
    

def main():
    n=input()
    aDict={}
    for i in range(int(n)):
        s=input()
        l=s.split()
        if l[0][0] not in aDict:
            aDict[l[0][0]]=[l[1]]
        else:
            aDict[l[0][0]].append(l[1])
    print(biggest(aDict))

if __name__== "__main__":
    main()