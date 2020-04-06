def start():
    people_dictionary = {'brett' : ['Male' , 'Weight 175'],
                     'nancy' : ['Female' , 'Weight 125'],
                     'patrick' : ['Male' , 'Weight 195'],
                     'diane' : ['Female' , 'Weight 115'],
                     'adam' : ['Male' , 'Weight 215']}
    print(people_dictionary)
    Name = input('please type your name: ').lower()
    print('Your name is ' + Name.capitalize())
    Persons_Data = people_dictionary[Name]
    try:
        Persons_Data = people_dictionary[Name]
        print('Name: ' + Name.capitalize())
        print('Sex: ' + Persons_Data[0])
        print('Weight: ' +Persons_Data[1])
        more()
    except:
        print('That name, ' + (Name) + 'was not found in the dictionary')
        more()
    def more():
        More = input('Would you like to search for another name?: ')
        if More == 'No':
            quit()
        if More == 'Yes':
            start()
        else:
            print('please ender "Yes" or "No"')
            more()
start()


