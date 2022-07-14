first_name="ada"
last_name="lovelace"
full_name=f"{first_name} {last_name}" #f字符串——在字符串中使用变量

print("Hello,", full_name.title())
print(f"Hello, {full_name.title()}")

message=f"Hello, {full_name.title()}"
print(message)

print("Python")
print("\tPython")                  #制表符\t
print("\nPython")                  #换行符\n
print("Languages:\nPython")

favorite_language=" python "
print(favorite_language)
print(favorite_language.rstrip()) #删除字符串末尾空白rstrip()
print(favorite_language.lstrip()) #删除字符串开头空白lstrip()
print(favorite_language.strip())  #删除字符串两边空白strip()