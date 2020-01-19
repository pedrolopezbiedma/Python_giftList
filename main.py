### Imports ###
from Classes.Persons import Persons
from Classes.MenuAux import showLovelyWelcome, showMenuOptions, showLovelyGoodBye

### Class Instances
personList = Persons()

### Local variables ###
menuOption = ''
updatePersonList = ''

### Main Program ###
showLovelyWelcome()

while(menuOption != '0'):
    showMenuOptions()
    menuOption = input('>>> Choose an option from the previous ones:')
 
    print('\n')
    if(menuOption == '1'):
        personList.printPersonList()
        updatePersonList = ''

        ### Giving the option to add persons.
        while(updatePersonList != 'n'):
            updatePersonList = input('Do you want to add another person? (y/n): ')
            if(updatePersonList == 'y'):
                person = input('Please type the name of the new person: ')
                personList.addPerson(person)

    elif(menuOption == '2'):
        print(f'You chose {menuOption}')
    elif(menuOption == '3'):
        print(f'You chose {menuOption}')
    elif(menuOption == '4'):
        print(f'You chose {menuOption}')
    elif(menuOption == '0'):
        showLovelyGoodBye()
    else:
        print('Choose a correct option please.')