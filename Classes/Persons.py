class Persons:

    def __init__(self):
        self.personList = ['Pedro','Lucia']
    
    def addPerson(self, person):
        self.personList.append(person)

    def personFound(self, person):
        for p in self.personList:
            if(p == person):
                return True;

        return False;

    def printPersonList(self):
        if(len(self.personList) > 0):
            print('*** Person List ***')
            for person in self.personList:
                print(person)
        else:
            print('There are no persons yet, you might want to add some ;)')