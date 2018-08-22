#define the simple_divide function here
def simple_divide(item, denom):
    # start a try-except block
    try:
    	return item/denom
    except ZeroDivisionError:
    	print([item/denom])
   
def fancy_divide(l1, index):
    denom = l1[index]
    return [simple_divide(item, denom) for item in l1]


def main():
	data = raw_input()
	l=data.split()
	l1=[]
	for j in l:
		l1.append(float(j))
	s=raw_input()
	index=int(s)
	print(fancy_divide(l1,index))
	

if __name__== "__main__":
	main()
