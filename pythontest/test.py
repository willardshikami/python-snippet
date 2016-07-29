def getName():
        testName = str(raw_input("What is your name?"))
        names = open('name.txt', 'r')
        name_list = []
        for name in names:
                name_list.append(names)
                for input_name in name_list:
                    if name != name_list[input_name]:
                        return 'wrong name'
                    return 'welcome' + name_list[input_name]
    
