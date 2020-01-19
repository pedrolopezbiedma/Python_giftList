### Imports ###
from Classes.Persons import Persons
from Classes.GiftList import GiftList
from Classes.MenuAux import showLovelyWelcome, showMenuOptions, showLovelyGoodBye

### Class Instances
personList = Persons()
giftList = GiftList()

### Local variables ###
menuOption = ''
updatePersonList = ''
personForGift = ''

### Main Program ###
showLovelyWelcome()

while(menuOption != '0'):
    showMenuOptions()
    menuOption = input('>>> Choose an option from the previous ones:')
 
    print('\n')
    if(menuOption == '1'): # Show person list
        personList.printPersonList()
        updatePersonList = ''

        ### Giving the option to add persons.
        while(updatePersonList != 'n'):
            updatePersonList = input('Do you want to add another person? (y/n): ')
            if(updatePersonList == 'y'):
                person = input('Please type the name of the new person: ')
                personList.addPerson(person)

    elif(menuOption == '2'): # Show gift list
        giftList.printGiftList()

    elif(menuOption == '3'): # Add a gift to a person
        personList.printPersonList()
        personForGift = input('For whom do you want to add a gift?')
        if(personList.personFound(personForGift)):
            print('Hola')
        else:
            print('That person is not in the list, you\'ll have add it first :( )')

    elif(menuOption == '4'):
        print(f'You chose {menuOption}')
    elif(menuOption == '0'):
        showLovelyGoodBye()
    else:
        print('Choose a correct option please.')