# 存储所点比萨的信息
pizza = {
    'crust':'thick',
    'toppings':['mushrooms','extra cheese'],    #在字典中存储列表
    }
# 概述所点的比萨
print(f"You ordered a {pizza['crust']}-crust pizza"    #如果函数调用print()中的字符串很长，可以在合适的位置分行。只需要在每行末尾都加上引号，同时对于除第一行外的其他各行，都在行首加上引号并缩进，这样，Python将自动合并圆括号内的所有字符串
    " with the following toppings:")

for topping in pizza['toppings']:
    print('\t'+topping)