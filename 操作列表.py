magicmans=['David','alice','carolina']
for magicman in magicmans:
    print(magicman)
#使用range(n,m)创建数字列表,包前不包后
for values in range(1,7):
    print(values)
#将range转为集合
numbers=list(range(1,7))
for number in numbers:
    print(number)
#第三个参数设置步长
for number in range(1,11,2):
    print(number)
#统计计算
names=['bruce','xack','leon']
digits=[1,2,3,4,5]
print(min(names))
print(max(names))
print(sum(digits))
#一句话列表解析
square=[value**2 for value in range(1,11)]
print(square)
#截取列表:切片[初始位置:结束位置]包钱不包后
players=['charles','martina','michael','eli','florence']
print(players[0:3])
print(players[:3])#不加开头就是从第一个元素开始
print(players[0:])#不加结束的位置就是到最后结束
print(players[-3:-1])#倒数第三个到倒数第二个
#列表的复制
foods=['ice cream','meat','apple']
friend_food=foods
foods.append("banbana")
print(foods)
print(friend_food)
#上面的这中两个列表都指向一个地址，所以不算一种复制
#复制1
friend_food1=foods[:]
#复制2
friend_food2=foods.copy()
foods.append("chololate")
print(foods)
print(friend_food2)
print(friend_food1)
#检查某个集合中是否有指定值
print("pears" in foods)#false
print("pears" not in foods)#True