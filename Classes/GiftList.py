class GiftList:

    def __init__(self):
        self.listDict = { 'Pedro': [ 'Mando', 'Gafas' ], 'Lucia':[ 'Luci1', 'Lucia2'] }
    
    def addGift(self, person, gift):
        if(person in list(self.listDict.keys())):
            giftList = list(self.listDict[person])
            giftList.append(gift)
            self.listDict[person] = giftList
        else:
            self.listDict[person] = []
            self.listDict[person].append(gift)

    def printGiftList(self):
        print('--------------------------- Gifts List -----------------------------')
        for person in list(self.listDict.keys()):
            print(f'| *** Presents for {person} ***')
            for gift in list(self.listDict[person]):
                print(f'|{gift}')
            print('|')
        print('--------------------------------------------------------------------')

    def printPersonGifts(self, person):
        if(person in list(self.listDict.keys())):
            print(f'----------------------------- {person}\'s Gifts --------------------------------')
            for gift in list(self.listDict[person]):
                print(f'| {gift}')
            print('--------------------------------------------------------------------')
        else:           
            print(f'{person} doesn\'t have presents yet, add one!!!')