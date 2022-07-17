alien_0={'color':'green','points':'5'}
alien_1={'color':'yellow','points':'10'}
alien_2={'color':'red','points':'15'}

aliens=[alien_0,alien_1,alien_2]    #列表中嵌套字典
for alien in aliens:
    print(alien)

# 创建30个绿色的外星人
aliens=[]
for alien_number in range(30):    #循环30次
    new_alien = {'color':'green','points':'5','speed':'slow'}
    aliens.append(new_alien)

# 显示前5个外星人
for alien in aliens[:5]:
    print(alien)
print("...")

# 显示创建了多少个外星人
print(f"Total number of aliens:{len(aliens)}")

for alien in aliens[:3]:    #修改前3个外星人
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['points'] = '10'
        alien['speed'] = 'medium'

for alien in aliens[:5]:
    print(alien)
print("...")