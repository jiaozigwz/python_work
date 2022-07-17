players=['charles','martina','michael','florence','eli']
print(players[0:3])
print(players[1:4])
print(players[:4])
print(players[2:])
print(players[-3:])     #输出名单上的最后三名队员
print(players[0::3])    #步长为3

print("Here are the first three players on my team:")
for player in players[:3]:     #使用for循环遍历切片
	print(player.title())