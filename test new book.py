import copy
import math
id(1)
print(id(1))  # 在ram里面的位置

# type(3)
# type(3.0)

# '24980128468964816481489812222'
# 2 ** 1000
# print(2 ** 1000)

# print(2/5)
# print(7/2)
# print(10.0 / 3)

# print(5/2)
# print(5 % 2)

# print(math.pi)
# print(dir(math))
# print(math.pow)
# print(math.pow(4, 2))
print("3" + "5")
a = 1996
b = "test"
print(b + str(a))

lang = "study python"
c = lang[1:11]  # 是减在1和11的位置的字起来
print(c)
print(id(lang))  # ID是看这个str在ram的位置
print(id(c))

str1 = 'gary'
str2 = 'cheah'
print(str1+str2)
print(str1 + "-->"+str2)
print("a" in str1)
print("h"in str2)
print("o"in str1)

# 最值（大或小）
print(max(str1))  # print 数字或者字体最大 最值
print(max(str2))
print(min(str1))  # print最小的
z = ["adam", "ballon", "cat"]
print(min(z))  # 完整字体也可以用（物体int就不能）
print(max(z))
# 比较用的（目前不是很明白）
print(ord('g'))  # 如果字体就不能，目前还不知道原因
print(ord(' '))
print(chr(103))  # g的数字是103 把chr（103）会变会g

print(str1*3)  # 可以填写3次（符号也是可以）

y = "hello you"  # str
print(len(y))  # 电脑会算出字体的长度，现在字体还是str
print(type(y))

x = len(y)  # 如果这样做会把str改称int
print(type(x))
print(x)

w = "my name is gary"
print(w.split(" "))  # 字体会分开起来（['my', 'name', 'is', 'gary']）

v = " can i go inside "
print(v.lstrip())  # 删掉前面的空格
print(v.rstrip())  # 删掉后面的空格
print(v.strip())  # 删掉前后多余的空格（这个会比较常用）

print(v.lstrip().capitalize())  # 把第一一个字变大号
print(v.lstrip().capitalize().istitle())
j = " Hi"
print(j.istitle())  # 检查第一个字体是不是大号 （可以检查连着的字）

print("i like %s" % "u")  # 在要改的字体添加%s 是方便为了要增加或者更改句子

number = [1, 2, 3, 4]
number.insert(3, 8)  # 前面d的3是让后面的8加在那个位置
print(number)  # 可以insert数字罢了，字体尝试了不能，字体要用回appand

all_user = ['keat', 'peng', 'ah hai', 'liang', 'keat', 'keat']
all_user.remove('keat')  # 如果有其他的也是删除其中一个罢了
all_user.remove('keat')  # remove可以累积删除
print(all_user)

ad = {}
ad["name"] = 'gary'  # ad的名称就是gary的意识
ad['age'] = '23'  # 可以累加 {'name': 'gary', 'age': '23'}
print(ad)  # 会显示{'name':'gary'}

ac = (["gary", "cheah"], ["cheah", "jinkeat"])
name = dict(ac)
print(ac)  # 出来的答案没有变化位置

ae = dict(name="gary", age=23)  # 也是没有变化
print(ae)

jk = {"name": "gary", "age": ["1", "me", "24"]}
keat = jk.copy()  # copy分开出来，如果有如何更改不会影响到jk那边会save在2个不同的id里面
print(keat)
print(jk)
# 前面一定要标明keat或者jk这样，没有的话会说没有这个名称 (但是在keat那边洗了jk那边也是不见了)（要用deepcopy,看113那边）
keat["age"].remove("me")  # 数字或者字体都可以
print(keat)
keat["name"] = "cheah jin keat"  # 可以更改名称用这样的方式
print(keat)
jk["name"] = "gary cheah"  # 如果copy的对象改了，copy那边会跟着改
print(jk)
print(keat)
gc = copy.deepcopy(jk)  # deepcopy 后面不可以忘记放在（）不然只会出现数字罢了
print(gc)
gc["name"] = "gary cheah jin keat"
print(gc)
print(jk)
print(keat)
