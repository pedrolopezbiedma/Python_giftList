class GiftList:

    def __init__(self):
        self.listDict = { 'Pedro': [ 'Mando', 'Gafas'], 'Lucia':[ 'Luci1', 'Lucia2'] }
    
    def printGiftList(self):
        for person in list(self.listDict.keys()):
            for gift in list(self.listDict[person]):
                print(f'Regalo de {person} es: {gift}')
