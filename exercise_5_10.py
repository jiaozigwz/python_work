current_users=['admin','Jiaozi','dandan','mumu','yaoyao']
new_users=['jiaozi','dAndan','miaomiao','tiaotiao','tiantian']
current_users_lower=[]
for user in current_users:
    user = user.lower()
    current_users_lower.append(user)

for user in new_users :
    if user.lower() in current_users_lower :
        print(f"用户名{user}重复，请重新输入！")
    else :
        print(f"用户名{user}未被使用")
