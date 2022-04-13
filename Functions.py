import time

def HangmanGraphic(i):
    if i == 0:
        print('''
 ___________.._______
| .__________))______|
| | / /      ||
| |/ /       ||
| | /        ||
| |/         ||  
| |          ||  
| |          ()
| |        
| |       
| |       
| |     
| |     
| |        
| |          
| |         
| |        
| |        
 ''')

    elif i == 1:
        print('''
 ___________.._______
| .__________))______|
| | / /      ||
| |/ /       ||
| | /        ||.-''.
| |/         |/  _  |
| |          ||  `/,|
| |          (\|`_.'
| |         
| |         
| |      
| |   
| |     
| |          
| |         
| |          
| |          
| |         ''')

    elif i == 2:
        print('''
 ___________.._______
| .__________))______|
| | / /      ||
| |/ /       ||
| | /        ||.-''.
| |/         |/  _  |
| |          ||  `/,|
| |          (\|`_.'
| |         .-`--'.
| |        |_ . . _|
| |          |   | 
| |          | . |
| |          |   |   
| |           ---
| |          
| |          
| |          
| |         ''')

    elif i == 3:
        print('''
  ___________.._______
| .__________))______|
| | / /      ||
| |/ /       ||
| | /        ||.-''.
| |/         |/  _  |
| |          ||  `/,|
| |          (\|`_.'
| |         .-`--'.
| |        /Y . . _|
| |       // |   | 
| |      //  | . |  
| |     ')   |   |   
| |           ---
| |         
| |          
| |          
| |         ''')

    elif i == 4:
        print('''
 ___________.._______
| .__________))______|
| | / /      ||
| |/ /       ||
| | /        ||.-''.
| |/         |/  _  |
| |          ||  `/,|
| |          (\|`_.'
| |         .-`--'.
| |        /Y . . Y|
| |       // |   | \|
| |      //  | . |  \|
| |     ')   |   |   (`
| |           ---
| |          
| |          
| |          
| |         ''')

    elif i == 5:
        print('''
 ___________.._______
| .__________))______|
| | / /      ||
| |/ /       ||
| | /        ||.-''.
| |/         |/  _  |
| |          ||  `/,|
| |          (\|`_.'
| |         .-`--'.
| |        /Y . . Y|
| |       // |   | \|
| |      //  | . |  \|
| |     ')   |   |   (`
| |          ||'-
| |          || 
| |          || 
| |          || 
| |         / | ''')

    elif i == 6:
        print('''
 ___________.._______
| .__________))______|
| | / /      ||
| |/ /       ||
| | /        ||.-''.
| |/         |/  _  |
| |          ||  `/,|
| |          (\|`_.'
| |         .-`--'.
| |        /Y . . Y|
| |       // |   | \|
| |      //  | . |  \|
| |     ')   |   |   (`
| |          ||'||
| |          || ||
| |          || ||
| |          || ||
| |         / | | |''')

def EndingFunction():
    time.sleep(0.5)
    print("\n")
    time.sleep(0.5)
    print("\n")
    time.sleep(0.5)
    print("\033[1;33;40m             ___________")
    time.sleep(0.15)
    print("\033[1;33;40m            '._==_==_=_.'")
    time.sleep(0.15)
    print("\033[1;33;40m            .-\:      /-.")
    time.sleep(0.15)
    print("\033[1;33;40m           | (|:.     |) |")
    time.sleep(0.15)
    print("\033[1;33;40m            '-|:.     |-'")
    time.sleep(0.15)
    print("\033[1;33;40m              \::.    /")
    time.sleep(0.15)
    print("\033[1;33;40m               '::. .'")
    time.sleep(0.15)
    print("\033[1;33;40m                 ) (")
    time.sleep(0.15)
    print("\033[1;33;40m               _.' '._")
    time.sleep(0.15)
    print('\033[1;33;40m              `"""""""` ')


def Menu():
    menu = True
    print("\n\n\033[1;34;40m                                                              WELCOME TO")
    print('''                                                                   
 .----------------. .----------------. .-----------------..----------------. .----------------. .----------------. .-----------------.
| .--------------. | .--------------. | .--------------. | .--------------. | .--------------. | .--------------. | .--------------. |
| |  ____  ____  | | |      __      | | | ____  _____  | | |    ______    | | | ____    ____ | | |      __      | | | ____  _____  | |
| | |_   ||   _| | | |     /  \     | | ||_   \|_   _| | | |  .' ___  |   | | ||_   \  /   _|| | |     /  \     | | ||_   \|_   _| | |
| |   | |__| |   | | |    / /\ \    | | |  |   \ | |   | | | / .'   \_|   | | |  |   \/   |  | | |    / /\ \    | | |  |   \ | |   | |
| |   |  __  |   | | |   / ____ \   | | |  | |\ \| |   | | | | |    ____  | | |  | |\  /| |  | | |   / ____ \   | | |  | |\ \| |   | |
| |  _| |  | |_  | | | _/ /    \ \_ | | | _| |_\   |_  | | | \ `.___]  _| | | | _| |_\/_| |_ | | | _/ /    \ \_ | | | _| |_\   |_  | |
| | |____||____| | | ||____|  |____|| | ||_____|\____| | | |  `._____.'   | | ||_____||_____|| | ||____|  |____|| | ||_____|\____| | |
| |              | | |              | | |              | | |              | | |              | | |              | | |              | |
| '--------------' | '--------------' | '--------------' | '--------------' | '--------------' | '--------------' | '--------------' |
 '----------------' '----------------' '----------------' '----------------' '----------------' '----------------' '----------------' 
    ''')
    while menu == True:

        i = input("                                                            Enter any key:\033[2;37m")
        if len(i) > 0:
            break
        else:
            continue





