### Imports ###
from Sources.Persons import Persons
from Sources.GiftList import GiftList
from Sources.MenuAux import showLovelyWelcome, showMenuOptions, showLovelyGoodBye, askMenuOption, askPerson, askGift, optionNotFound
from Sources.DocumentHandler import initialLoad

### Class Instances
giftList = GiftList()

### Local variables ###
menuOption = ''
typedPerson = ''
newGift = ''

### Main Program ###
#initialLoad(giftList)

showLovelyWelcome()
#menuOption = '0'

while(menuOption != '0'):
    showMenuOptions()
    menuOption = askMenuOption()

    if(menuOption == '1'):
        giftList.printPersonsInGiftList()
        giftList.askToUpdatePersonList()

    elif(menuOption == '2'):
        giftList.printGiftList()

    elif(menuOption == '3'):
        giftList.printPersonsInGiftList()
 
        typedPerson = askPerson('checkPersonGifts')
        giftList.printPersonGifts(typedPerson)

    elif(menuOption == '4'):
        giftList.printPersonsInGiftList()

        typedPerson = askPerson('addPersonGift')
        newGift = askGift()
        giftList.addGiftToPerson(typedPerson, newGift)

    elif(menuOption == '0'):
        showLovelyGoodBye()

    else:
        optionNotFound()
