""" abs """
def apply_to_each(L, f):
    return list(map(abs, L))
    
    
def main():
    """ abs """
    data = input()
    data = data.split(" ")
    list1 = []
    for j in data:
        list1.append(int(j))
    var = apply_to_each(list1, abs)
    print(var)
if __name__ == "__main__":
    main()