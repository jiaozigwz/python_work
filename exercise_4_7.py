numbers=[]
for value in range(3,31):
	number=value%3
	if number==0:
		numbers.append(value)
print(numbers)

threes=list(range(3,31,3))   #标准答案
for number in threes:
	print(number)