#定义一个基本的字典
alien={'color':'red','point':5}
print(alien['color'])
print(alien['point'])
#键值对key-value
#增加键值对
alien["name"]="ET"
print(alien)
#修改
alien["name"]="ET1"
print(alien)
#删除键值对
del alien["name"]#永久删除消失
print(alien)
#遍历字典
user_0={
    'name':"Bruce",
    'age':23,
    'likeSport':'baksetball',
}
for k,v in user_0.items():
    print(k)
    print(v)
#只打印键
for key in user_0.keys():
    print(key+"is"+str(user_0[key]))
#利用popitem删除最后一个元素,返回删除的键值对形成的字典
print(user_0.popitem())
print(user_0)
#pop必须带有参数，返回key对应的值
print(user_0.pop("name"))
print(user_0)
age=[13,34,56,78,13,34]
#利用set集合去除重复
print(set(age))
####################################################################
##############外星人项目##########################################
#创建30个外星人
aliens=[]
for alien_number in range(30):
    aliens.append({'color':'green','point':5,'speed':'slow'})
for alien in aliens[:5]:
    print(alien)
print("......")
print("Total number of alien is "+str(len(aliens)))