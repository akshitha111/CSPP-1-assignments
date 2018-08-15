s1 = input()
s2 = "bob"
count = 0

for i in range(len(s1-2)):
	if s1[i]+s1[i+1]+s1[i+2] == s2:
		count = count+1
print(count)