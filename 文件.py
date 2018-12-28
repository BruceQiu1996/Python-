#这种方式不需要关闭文件流，并且设置定了编码
with open("info.txt",encoding='utf-8') as file_object:
    contents=file_object.read()
    print(contents)
#方式二
fstr=open("info.txt",encoding='utf-8')
print(fstr.read().rstrip())
fstr.close()
print(fstr.closed)
#逐行打印文件
try:
    with open("info1.txt",encoding='utf-8') as file_object:
        for line in file_object:
            print(line.rstrip())
except Exception as ex:
    print(ex)
else:
    print("执行成功!")
#利用json写入
import json
numbers=[1,2,3,4,5]
with open("info.txt",encoding='utf-8',mode='a') as file_object:
      json.dump(numbers,file_object)
