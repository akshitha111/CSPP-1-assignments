data=((1,2),(3,4),(5,8),(7,6))
def fun(m):
    v = data[0][0]
    for row in m:
        for ele in row:
            if v<ele:
                v = ele
    return v
print(fun(data))