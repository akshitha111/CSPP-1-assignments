""" square """
def square(x_1):
    """ square """
    return x_1*x_1
def apply_to_each(L, square):
    """ square """
    return list(map(square, L))
def main():
    """ square """
    data = input()
    data = data.split(" ")
    list1 = []
    for j in data:
        list1.append(int(j))
    print(apply_to_each(list1, square))
if __name__ == "__main__":
    main()
