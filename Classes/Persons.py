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
            print('**************************** Person List ***************************')
            for person in self.personList:
                print(f'| {person} ')
            print('********************************************************************')
        else:
            print('There are no persons yet, you might want to add some ;)')

    def askToUpdatePersonList(self):
        updatePersonList = ''

        while(updatePersonList != 'n'):
            updatePersonList = input('Do you want to add another person? (y/n): ')
            print('\n')

            if(updatePersonList == 'y'):
                person = input('Please type the name of the new person: ')
                self.addPerson(person)
            self.printPersonList()
