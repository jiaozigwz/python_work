# 人们
person_1={'姓':'狗','名':'蛋','年龄':'18','城市':'上海'}
person_2={'姓':'猪','名':'猪','年龄':'17','城市':'四川'}
person_3={'姓':'天','名':'天','年龄':'16','城市':'浙江'}

people=[person_1,person_2,person_3]

for person in people:
    name=f"{person['姓']}{person['名']}"
    age=person['年龄']
    city=person['城市']
    print(f"{name}今年{age}岁，来自{city}。")