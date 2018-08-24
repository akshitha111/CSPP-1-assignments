s = str(input())
vowels = ['a','e','i','o','u']
count = 0
for i in vowels:
	if i in s:
		count = count+1
print(count)