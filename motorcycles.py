motorcycles=[]
motorcycles.append('honda')     #用append方法将元素添加到列表末尾
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print(motorcycles)

motorcycles.insert(0,'ducati')   #用insert方法将元素插入到任意位置
print(motorcycles)

del motorcycles[0]   #用del删除列表中的任意元素，不再以任何方式使用它
print(motorcycles)

popped_motorcycle=motorcycles.pop()   #使用pop方法删除列表末尾的元素，并让你接着使用它
print(motorcycles)
print(popped_motorcycle)
motorcycles.append('suziki')
motorcycles.append('ducati')

motorcycles.remove('ducati')    #使用remove方法根据值来删除列表中的元素，只删除第一个指定的值，如果要删除的值在列表中出现多次，就需要使用循环来确保将每个值都删除
print(motorcycles)
motorcycles.append('ducati')

too_expensive='ducati'     #使用remove方法从列表中删除元素时，通过将其赋值给一个变量，可以接着使用它的值
motorcycles.remove(too_expensive)
print(motorcycles)
print(f"\nA {too_expensive.title()} is too expensive for me.")