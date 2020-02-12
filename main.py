### Imports ###
from Classes.Persons import Persons
from Classes.GiftList import GiftList
from Classes.MenuAux import showLovelyWelcome, showMenuOptions, showLovelyGoodBye, askMenuOption, askPerson, personNotFound, askGift, optionNotFound

### Class Instances
personList = Persons()
giftList = GiftList()

### Local variables ###
menuOption = ''
typedPerson = ''
newGift = ''

### Local functions ###

### Main Program ###
showLovelyWelcome()

while(menuOption != '0'):
    showMenuOptions()
    menuOption = askMenuOption();

    if(menuOption == '1'):
        personList.printPersonList()
        personList.askToUpdatePersonList()

    elif(menuOption == '2'):
        giftList.printGiftList()

    elif(menuOption == '3'):
        personList.printPersonList()
        typedPerson = askPerson('checkPersonGifts')

        if(personList.personFound(typedPerson)):
            giftList.printPersonGifts(typedPerson)
        else:
            personNotFound()

    elif(menuOption == '4'):
        personList.printPersonList()
        typedPerson = askPerson('addPersonGift')

        if(personList.personFound(typedPerson)):
            newGift = askGift()
            giftList.addGift(typedPerson, newGift)
        else:
            personNotFound()

    elif(menuOption == '0'):
        showLovelyGoodBye()
        
    else:
        optionNotFound()
