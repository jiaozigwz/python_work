#修改嘉宾名单
name_list=['蛋蛋1号','蛋蛋2号','蛋蛋3号']
print(f"很遗憾，刚接到通知，{name_list[0]}今晚有事无法赴约")
del name_list[0]
name_list.append('蛋蛋4号')
print(f"诚邀{name_list[0]}与饺子先生于7月14日晚六点在香格里拉共进晚餐")
print(f"诚邀{name_list[1]}与饺子先生于7月14日晚六点在香格里拉共进晚餐")
print(f"诚邀{name_list[2]}与饺子先生于7月14日晚六点在香格里拉共进晚餐")
