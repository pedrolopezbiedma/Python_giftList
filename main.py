### Imports ###
from Sources.GiftList import GiftList
from Sources.MenuAux import showLovelyWelcome, showMenuOptions, showLovelyGoodBye, askMenuOption, askPerson, askGift, optionNotFound

### Class Instances
giftList = GiftList()

### Local variables ###
menuOption = ''
typedPerson = ''
newGift = ''

### Local Methods ###
def loadFile():
    with open('Giftlist/output.txt') as output_file:
        lines = output_file.readlines();
        personName = ''
        desires = []
        nameObtained = False
        giftObtained = False

        for line in lines:
            if(line[0] == '*'): # Line with name
                personName = line[2:].strip()
                giftList.addPersonToGiftList(personName)
                nameObtained = True

            elif(line[0] != '-'):
                if(nameObtained == True): # We already have the name, so we're getting desires
                    giftList.addGiftToPerson(personName, line.strip())
                    giftObtained = True

            if(line[0] == '-' and giftObtained == True):
                personName = ''
                nameObtained = False
                giftObtained = False

def writeFile():
    dictionary = giftList.getCompleteGiftList()
    with open('Giftlist/output.txt', 'w') as output_file:
        output_file.write('##################################################' + '\n')
        output_file.write('#################### Gift List ###################' + '\n')
        output_file.write('##################################################' + '\n')
        for person in list(dictionary.keys()):
            output_file.write('--------------------------------------------------' + '\n')
            output_file.write('* ' + person + '\n')
            for gift in list(dictionary[person]):
                output_file.write(gift + '\n')

### Main Program ###

showLovelyWelcome()
loadFile()

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

    elif(menuOption == '5'):
        writeFile()

    elif(menuOption == '0'):
        showLovelyGoodBye()

    else:
        optionNotFound()
