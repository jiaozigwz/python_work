alien_0={'color':'green','speed':'slow'}

point_value=alien_0.get('points','No point value assigned.')    
#使用get()方法在指定的键不存在时返回一个默认值，从而避免报错

print(point_value)