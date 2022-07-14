#缩减名单
print("很遗憾，由于某些不可告人的原因，今晚只能邀请两位嘉宾与我共进晚餐")
name_list=['蛋蛋5号','蛋蛋2号','蛋蛋6号','蛋蛋3号','蛋蛋4号','蛋蛋7号']
print(f"很遗憾，{name_list.pop()}，无法邀请你与我共进晚餐")
print(f"很遗憾，{name_list.pop()}，无法邀请你与我共进晚餐")
print(f"很遗憾，{name_list.pop()}，无法邀请你与我共进晚餐")
print(f"很遗憾，{name_list.pop()}，无法邀请你与我共进晚餐")
print(f"恭喜你，{name_list[0]}，今晚可以与饺子先生共进晚餐！")
print(f"恭喜你，{name_list[1]}，今晚可以与饺子先生共进晚餐！")
del name_list[0]
del name_list[0]
print(name_list)