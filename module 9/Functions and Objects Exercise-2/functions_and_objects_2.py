""" add """
def f(x):
    """ add """
    return x+1
def apply_to_each(L, f):

    return list(map(f,L))   
def main():
    """ add """
    data = input()
    data = data.split(" ")
    list1 = []
    for j in data:
        list1.append(int(j))
    print(apply_to_each(list1, f))
if __name__ == "__main__":
    main()
