name = 'Garycheah'
password = '123456'

while True:

    name = input('Please type your name.')
    if name.lower() != 'gary cheah':  # 如果名字是gary cheah就继续往下走
        continue
    else:
        print('Thank you.')

    # {name.titile()}是自动拿上面的名称  如果前方加f后面就不需要一直用➕了
    print(f'Hello,{name.title()}. What is the password? (It is a fish.)')

    password = ""
    while password != 'swordfish':  # 轮回
        password = input("Please enter password. ")
        if password == 'swordfish':
            print('access grated')
            break
        else:
            print("wrong password")
    break
