def chapter1():
    name = ['khoo', 'lim', 'cheah']
    name.append('ooi')
    name.append('ng')
    name.append('cheah')
    name.append('chan')
    print(name)
    del name[0]
    popped_name = name.pop()
    print(popped_name)
    print(name)
    name.append('wong')
    name.remove('lim',)
    print(name)
    messsage = "welcome come to this event"
    print(messsage + " " + 'Mr ' + " " + popped_name.title() + '.')
    print(messsage + " " + 'Mr ' + popped_name.title() + '.')