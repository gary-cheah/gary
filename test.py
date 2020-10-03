import yourname


def main():
    test2


from chapter1 import chapter1





def g_sheet():
    # region hide
    import ezsheets

    # define google sheet file
    ss = ezsheets.Spreadsheet('17IuuYN-v7bzRYyJ8V4IDZVFYhEIUcTAPmGrhoFaLoKE')
    sheet = ss['ah lim ecu claim']

    # Declare variables
    x = 0
    result = []

    # result[][] to insert to db (list of lists)
    for i in range(1, 50):
        x += 1
        result.append(tuple(sheet.getRow(i)[:10]))

    new_result = []
    new_string = ""
    for x in result:
        if x[0] != "":
            if '9.1.1' in str(x[4]):
                new_string = x[4].replace('9.1.1', 'ecu 9.1.1')
                new_result.append(new_string)

    print(new_result)
    # endregion


def new():
    name = 'gary'
    password = '123456'

    if name == 'gary':  # 可以更改，然后会跟着更改发生变化
        print('welcome load in')

    elif name <= ('gary'):  # 如果不是这个标题会显示以下的内容
        print("id cant load in")

    if password == 'abc':  # 可以更改，然后会跟着更改发生变化
        print("load in")

    elif password <= ('123456'):  # 如果不是这个标题会显示以下的内容
        print('cant load in')

    a = ["1", "2", "3", "4"]
    for gc in a:
        print(gc)

    for gc in range(0, 6):  # 如果设置了range会到达设定的分量就会停下或者次数
        print("hello")  # 一下这个设定会print6次hello然后停下来了/如果是（“0，6”）就会顺序排列

    # break 中断循环
    a = ["1", "2", "3", "4"]
    for gc in a:
        if(gc == "3"):
            break  # 如果这样设定会直接在3那边就停了
        print(gc)

    # continue 跳过指定然后继续
    a = ["1", "2", "3", "4"]
    for gc in a:
        if(gc == "3"):
            continue  # 如果这样设定会直接在3那边会跳过然后继续
        print(gc)

        print('My name is')
        for i in range(5):  # （for=关键字）i是显示后面0-4的次数，我尝试删了i会出现错误
            print('gary(' + str(i) + ')')  # str 是排列吗？


main()
