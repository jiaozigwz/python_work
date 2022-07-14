magicians=['alice','david','carolina']
for magician in magicians:    #使用for循环打印名单中的所有名字
	print(magician)

for magician in magicians:
	print(f"{magician.title()}, that was a great trick!")
	print(f"I can't wait to see your next trick, {magician.title()}.\n")
print("Thank you, everyone. That was a great magic show!")