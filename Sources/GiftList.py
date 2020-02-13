class GiftList:

    def __init__(self):
        self.listDict = { 'Pedro': [ 'Mando', 'Gafas' ], 'Lucia':[ 'Luci1', 'Lucia2'] }

    def personFoundInList(self, person):
        for p in self.listDict.keys():
            if(p == person):
                return True;

        return False;       

    def addGiftToPerson(self, person, gift):
        if(self.personFoundInList(person)):
            giftList = list(self.listDict[person])
            giftList.append(gift)
            self.listDict[person] = giftList
        else:
            print(f'{person} is not in the list, add him/her first ;) !!!')

    def askToUpdatePersonList(self):
        updatePersonList = ''

        while(updatePersonList != 'n'):
            updatePersonList = input('Do you want to add another person? (y/n): ')
            print('\n')

            if(updatePersonList == 'y'):
                person = input('Please type the name of the new person: ')
                self.addPersonToGiftList(person)
            self.printPersonsInGiftList()

    def addPersonToGiftList(self, person):
        if(self.personFoundInList(person)):
            print('That person is already in the list, use another name.')
        else:
            self.listDict[person] = []

    def printPersonsInGiftList(self):
        print('**************************** Person List ***************************')
        for person in list(self.listDict.keys()):
            print(f'| {person} ')
        print('********************************************************************')

    def printPersonGifts(self, person):
        if(self.personFoundInList(person)):
            print(
                f'----------------------------- {person}\'s Gifts --------------------------------')
            for gift in list(self.listDict[person]):
                print(f'| {gift}')
            print('--------------------------------------------------------------------')
        else:
            print(f'{person} is not in the list, add him/her first ;) !!!')

    def printGiftList(self):
        print('--------------------------- Gifts List -----------------------------')
        for person in list(self.listDict.keys()):
            print(f'| *** Presents for {person} ***')
            for gift in list(self.listDict[person]):
                print(f'|{gift}')
            print('|')
        print('--------------------------------------------------------------------')
