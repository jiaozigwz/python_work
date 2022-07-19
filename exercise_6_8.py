# 宠物
pet_1={
    'kind':'dog',
    'master':'dandan',
    }

pet_2={
    'kind':'monkey',
    'master':'tiantian',
    }

pet_3={
    'kind':'cat',
    'master':'mumu',
    }

pets=[pet_1,pet_2,pet_3]

for pet in pets:
    kind=f"{pet['kind'].title()}"
    master=f"{pet['master'].title()}"
    print(f"{kind}的主人是{master}")