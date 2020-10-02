names = ['ah hai', 'ah liang', 'ah jack', 'asri', 'ah peng']
names.append("nora")
names.append("ah mie")
names.insert(0, "wei jie")
del names[4]
del names[2]
print(names)

for name in names:
    print(f"hi ,welcome to joint this parti, {name.title()}.")
for name in names:
    print(f"{name.title()} you will bring %s to %s?" %
          ("friend", "this parti"))


print("{o} now eat {eat}".format(o="ah hai", eat="mee"))
print("test {o} test{q}".format(o="1", q="ok"))

name1 = '海哥'
print(name1)
print(type(name1))
print(len(name1))

lst = [1, 2, 3]
print(lst.index(1))  # 读出字体在的位置

alst = ['a', 'b']
print(hasattr(alst, '__iter__'))  # 查看这个字体/数字可以不可以迭代
# 答案是true
