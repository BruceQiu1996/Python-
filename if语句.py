name="Bruce"
if name=="Bruce":
    print(True)
#比较时候不区分大小写
if name.lower()=="bruce":
    print(True)
print(name)
#多个提交的并逻辑
age=16
if age==19 and name=="Bruce":
    print(True)
if(age==20) or name=="Bruce":
    print(True)
#if-else
if age<18:
    print("you are young")
else:
    print("you are old")
#if-elif-else
if age>18:
    print("old")
elif age<14:
    print("young")
else:
    print("perfect")
#空列表直接返回false
foods=[]
if foods:
    print("what do u want")
else:
    print("no food")