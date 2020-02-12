### Imports ###
from Classes.Persons import Persons
from Classes.GiftList import GiftList
from Classes.MenuAux import showLovelyWelcome, showMenuOptions, showLovelyGoodBye, askMenuOption, askPerson, personNotFound, askGift, optionNotFound
from DocumentHandler import initialLoad

### Class Instances
personList = Persons()
giftList = GiftList()

### Local variables ###
menuOption = ''
typedPerson = ''
newGift = ''

### Main Program ###
initialLoad(giftList)

# showLovelyWelcome()
menuOption = '0'

while(menuOption != '0'):
    showMenuOptions()
    menuOption = askMenuOption();

    if(menuOption == '1'):
        giftList.printPersonsInGiftList()
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
