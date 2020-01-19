### Imports ###
from Classes.Persons import Persons
from Classes.GiftList import GiftList
from Classes.MenuAux import showLovelyWelcome, showMenuOptions, showLovelyGoodBye

### Class Instances
personList = Persons()
giftList = GiftList()

### Local variables ###
menuOption = ''
typedPerson = ''
newGift = ''

### Main Program ###
showLovelyWelcome()

while(menuOption != '0'):
    showMenuOptions()
    menuOption = input('>>> Choose an option from the previous ones: ')
 
    print('\n')
    if(menuOption == '1'): # Show person list
        personList.printPersonList()
        updatePersonList = ''

        ### Giving the option to add persons.
        while(updatePersonList != 'n'):
            updatePersonList = input('Do you want to add another person? (y/n): ')
            print('\n')
            
            if(updatePersonList == 'y'):
                person = input('Please type the name of the new person: ')
                personList.addPerson(person)
            personList.printPersonList()

    elif(menuOption == '2'): # Show gift list
        giftList.printGiftList()

    elif(menuOption == '3'): # Check gifts for a person
        personList.printPersonList()
        typedPerson = input('For whom do you want to check the gifts? ')
        if(personList.personFound(typedPerson)):
            giftList.printPersonGifts(typedPerson)
        else:
            print('That person is not in the list, you\'ll have add it first :( )')

    elif(menuOption == '4'): # Add a gift to a person
        personList.printPersonList()
        typedPerson = input('For whom do you want to add a gift? ')
        if(personList.personFound(typedPerson)):
            newGift = input('Please type the present you want to add: ')
            giftList.addGift(typedPerson, newGift)
        else:
            print('That person is not in the list, you\'ll have add it first :( )')

    elif(menuOption == '0'):
        showLovelyGoodBye()
    else:
        print('Choose a correct option please.')