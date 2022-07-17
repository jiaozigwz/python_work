my_foods=['饺子','锅贴','烧卖']
friend_foods=my_foods[:]
my_foods.append('辣肉面')
friend_foods.append('雪菜面')
print("我最喜欢吃的食物是：")
for food in my_foods:
	print(food)
print("\n朋友最喜欢的食物是：")
for food in friend_foods:
	print(food)