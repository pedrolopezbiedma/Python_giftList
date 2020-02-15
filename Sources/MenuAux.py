def showLovelyWelcome():
    print('**********************************************************************')
    print('********** Welcome to my wonderful Gift List python program **********')
    print('**********************************************************************')

def showMenuOptions():
    print('\n')
    print('----------------------------- Menu -----------------------------------')
    print('| 1.- Let\'s see the involved persons :)                              |')
    print('| 2.- Show me the entire Gift List                                   |')
    print('| 3.- I just want to check the gifts for one person                  |')
    print('| 4.- I want to add a gift to a person                               |')
    print('| 5.- Create a file with my gift list                                |')
    print('| 0.- Leave me alone, I just want to leave!!!                        |')
    print('----------------------------------------------------------------------')

def optionNotFound():
    print('Choose a correct option please.')

def askMenuOption():
    menuOption = input('>>> Choose an option from the previous ones: ')
    print('\n')

    return menuOption;

def askPerson(option):
    if option == 'checkPersonGifts':
        typedPerson = input('For whom do you want to check the gifts? ')

    elif option == 'addPersonGift':
        typedPerson = input('For whom do you want to add a gift? ')

    return typedPerson;


#def personNotFound():
#    print('That person is not in the list, you\'ll have add it first :( )')

def askGift():
    newGift = input('Please type the present you want to add: ')

    return newGift

def showLovelyGoodBye():
    print('**********************************************************************')
    print('************ Thanks a lot for using my beloved program <3 ************')
    print('**********************************************************************')
