cars=['bmw','audi','toyota','subaru']
cars.sort()    #使用sort方法对列表永久排序，按字母表顺序
print(cars)

cars.sort(reverse=True)    #向sort方法传递参数reverse=True，按字母表永久倒序排列
print(cars)

print(sorted(cars))    #使用函数sorted()对列表进行临时排序
print(sorted(cars,reverse=True))    #向函数sorted()传递参数reverse=True，按字母表倒序排列
print(cars)

cars=['bmw','audi','toyota','subaru']
print(cars)
cars.reverse()    #使用reverse方法反转列表的排列顺序
print(cars)

cars=['bmw','audi','toyota','subaru']
print(len(cars))    #使用函数len()获取列表的长度