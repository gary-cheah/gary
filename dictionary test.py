zd1 = {"gary": 24}
d2 = {"he work at sinriang trading": "as tuner"}
# update在d1的句子会增加，d2/d3的没有变化
d3 = {"4 YEAR": "Already"}
d1.update(d2)  # update可以累加起来，或者将字典里面的对象链接起来
d1.update(d3)
print(d1)
print(d3)
d = d1.copy()
print(d)
for key in d:
    print(d[key])  # 如果放d[key]会出来字典后面的答案，如果直接放key就会出现题目
d5 = set(["ah hai", "ah hai", "ah yang"])  # set可以整合起来然后不会print重复的东西出来
print(d5)
