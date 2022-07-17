# 以特殊方式跟管理员打招呼
user_list=['admin','jiaozi','dandan','mumu','yaoyao']
if user_list :
    for user in user_list :
        if user == 'admin' :
            print('Hello admin, would you like to see a status report?')
        else :
            print(f"Hello {user.title()}, thank you for logging in again.")
else :
    print('We need to find some users!')