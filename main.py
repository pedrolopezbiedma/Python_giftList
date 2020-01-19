# Gift list main menu.

filledUsers = False
menuOption = ''
persons = []
giftList = {}

print('**********************************************************************')
print('********** Welcome to my wonderful Gift List python program **********')
print('**********************************************************************')

while(menuOption != '0'):
    print('----------------------------------------------------------------------')
    print('| 1.- Let\'s see the involved persons :)                              |')
    print('| 2.- Show me the entire Gift List                                   |')
    print('| 3.- I want to add a gift to a person                               |')
    print('| 4.- I just want to check the gifts for one person                  |')
    print('| 0.- Leave me alone, I just want to leave!!!                        |')
    print('----------------------------------------------------------------------')
    menuOption = input('>>> Choose an option from the previous ones:')
 
    print('\n')
    if(menuOption == '1'):
        print(f'You chose {menuOption}')
    elif(menuOption == '2'):
        print(f'You chose {menuOption}')
    elif(menuOption == '3'):
        print(f'You chose {menuOption}')
    elif(menuOption == '4'):
        print(f'You chose {menuOption}')
    elif(menuOption == '0'):
        print('**********************************************************************')
        print('************ Thanks a lot for using my beloved program <3 ************')
        print('**********************************************************************')
    else:
        print('Choose a correct option please.')