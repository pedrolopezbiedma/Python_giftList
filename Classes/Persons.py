class Persons:

    def __init__(self):
        self.personList = ['Pedro','Lucia']
    
    def addPerson(self, person):
        self.personList.append(person)

    def checkPersonList(self):
        return True;

    def printPersonList(self):
        if(len(self.personList) > 0):
            print('*** Person List ***')
            for person in self.personList:
                print(person)
        else:
            print('There are no persons yet, you might want to add some ;)')