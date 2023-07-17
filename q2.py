st = str(input("Enter the string:  "))
dic = {}
for x in st:
	if(x in dic):
		dic[x]+=1
	else:
		dic[x]=1
print("Number of occurance of a letter in a sentence provided are given below: ")
print(dic)