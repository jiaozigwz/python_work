#添加嘉宾
name_list=['蛋蛋1号','蛋蛋2号','蛋蛋3号']
print(f"很遗憾，刚接到通知，{name_list[0]}今晚有事无法赴约")
del name_list[0]
name_list.append('蛋蛋4号')
print(f"诚邀{name_list[0]}与饺子先生于7月14日晚六点在香格里拉共进晚餐")
print(f"诚邀{name_list[1]}与饺子先生于7月14日晚六点在香格里拉共进晚餐")
print(f"诚邀{name_list[2]}与饺子先生于7月14日晚六点在香格里拉共进晚餐")

print("好消息，本人找到了一个更大的餐桌，因此可以多邀请三位嘉宾")
name_list.insert(0,'蛋蛋5号')    #将蛋蛋5号添加到名单开头
name_list.insert(2,'蛋蛋6号')    #将蛋蛋6号添加到名单中间
name_list.append('蛋蛋7号')      #将蛋蛋7号添加到名单末尾
print(f"诚邀{name_list[0]}与饺子先生于7月14日晚六点在香格里拉共进晚餐")
print(f"诚邀{name_list[1]}与饺子先生于7月14日晚六点在香格里拉共进晚餐")
print(f"诚邀{name_list[2]}与饺子先生于7月14日晚六点在香格里拉共进晚餐")
print(f"诚邀{name_list[3]}与饺子先生于7月14日晚六点在香格里拉共进晚餐")
print(f"诚邀{name_list[4]}与饺子先生于7月14日晚六点在香格里拉共进晚餐")
print(f"诚邀{name_list[5]}与饺子先生于7月14日晚六点在香格里拉共进晚餐")