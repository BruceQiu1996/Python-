#获取用户的输入
message=input("what's your name")
print(message)
#while循环
message1=int(message)
while int(message1)<5:
    print(message1)
    message1+=1
#continue结束本次循环，break结束循环
username=""
while username!="bruce":
    username=input("username:\t")
    if(username=='jack'):continue
    print(username)
password=""
while password!="12345":
    password=input("password:\t")
    if(password=='fuck'):break
    print(password)
#利用while循环处理列表和字典
#1:列表间移动元素
unfonfirm_user=['alice','brian','candace']
confirm_users=[]
while unfonfirm_user:
    current_user=unfonfirm_user.pop()
    confirm_users.append(current_user)
print("the following users have been confirmed:")
for user in confirm_users:
    print(user)
#2.利用while循环删除相同元素
pets=['dog','cat','rabbit','dog']
while 'dog' in pets:
    pets.remove('dog')
#利用while循环进行文件调查
replys={}
flag=True
while flag:
    username=input("what's your name can you tell me? ")
    reponse=input("can you come in my party(yes/no)")
    replys[username]=reponse
    answer=input("Any one can answer my question(yes/no)")
    flag=True if answer=="yes" else False
for key in replys.keys():
    print(key+("wants to" if replys[key]=="yes" else "don't wants to")+"join my party")