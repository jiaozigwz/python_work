my_foods=['pizza','falafel','carrot cake']
friend_foods=my_foods[:]    #复制列表[:]，得到是两张列表，而不是将my_foods赋值给friend_foods，如果用friend_foods=my_foods，那么两个变量指向同一个列表，对其中任意一个变量操作都会影响整个列表

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favorite foods are:")
for food in my_foods:
	print(food.title())
print("\nMy friend's favorite foods are:")
for food in friend_foods:
	print(food.title())