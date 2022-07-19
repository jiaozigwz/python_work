# 喜欢的地方
favorite_places={
    'jiaozi':['西藏','云南','新疆'],
    'dandan':['上海','浙江'],
    'tiantian':['四川','重庆']
    }

for name,places in favorite_places.items():
    print(f"\n{name.title()}喜欢的地方是：")
    for place in places:
        print(f"\t{place}")