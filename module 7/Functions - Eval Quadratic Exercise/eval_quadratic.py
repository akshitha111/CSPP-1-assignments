"""Solving Quadratic Equation."""
def eval_quadratic(a_1, b_1, c_1, x_1):
    """ quadratic """
    d_1 = (a_1*x_1**2) + (b_1*x_1) + (c_1)
    return d_1
def main():
    """ quadratic """
    data = input()
    data = data.split(' ')
    data = list(map(float, data))
    l_1 = len(data)
    # print(data)
    for x_1 in range(l_1):
        temp = str(data[x_1]).split('.')
        if temp[1] == '0':
            data[x_1] = int(float(str(data[x_1])))
        else:
            data[x_1] = data[x_1]
    print(eval_quadratic(data[0], data[1], data[2], data[3]))
if __name__ == "__main__":
    main()
