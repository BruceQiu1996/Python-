from 函数模块 import get_user_name as get_name
#定义一个函数
def greet_user():
    print("hello world")
greet_user()
#定义一个带有参数的函数
def show_name(username):
    print(username)
show_name('bruce')
#关键字实参
def show_age(age):
    print(str(age))
show_age(age=19)
#参数默认值
def pet_info(name,pettype='dog'):
    print(name+" is a "+pettype)
#以下打印是等效的
pet_info("alice")
pet_info("alice",'dog')
pet_info(name='alice')
pet_info(name='alice',pettype='dog')


#带有返回值的
def sum(a,b):
    return a+b
#传递进入列表
list1=['pizza','kfc','babecu']
current_food=[]
def remove_list(foods):
    while foods:
        current_food.append(foods.pop())
remove_list(list1)
print(list1)
print(current_food)
#如果不想改变原来列表，可以传递列表的copy
remove_list(list1[:])
#参数前加星号表示任意的参数,多个参数在一个元组中
def print_foods(*foods):
    for item in foods:
        print(item)
print_foods('kfc','pizza','fish')
#将函数存储到模块中,别名
print(get_name())

