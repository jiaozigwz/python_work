squares=[]
for value in range(1,11):
	square=value**2
	squares.append(square)
print(squares)

squares=[]
for value in range(1,11):
	squares.append(value**2)    #这种方法比上面的更加简洁
print(squares)

squares=[value**2 for value in range(1,11)]    #使用列表解析创建平方数表，这种方法最简单
print(squares)