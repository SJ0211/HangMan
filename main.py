
import time  #import time

def GuessFunction():           #Function for guessing
    global Counter
    global UsedWords
    global Wordlist

    Input = True
    while Input == True:        #start loop
        guess = input("What letter? : ")  # ask for a letter
        Guess = guess.upper()             # make it all capital letters
        if UsedWords.count(Guess) > 0:    # check if it was used already
            print("You used this word!")  # print this when used, then go loop
            continue
        elif len(Guess) > 1:                    #if entered more than
            print("please enter 1 letter")      #loop if it is
            continue
        elif Guess == ' ':
            print("Do not enter space!")        #no space
            continue
        else:
            Input = False                       #if ok, break the loop



        UsedWords.append(Guess)                 # add it to used list
        if Wordlist.count(Guess) > 0:           # is its right
            print("You got it!\n\n\n")          

            for p in [p for p, x in enumerate(Wordlist) if x == Guess]:             # These 3 lines replace the underscore
                Displaylist.pop(p)
                Displaylist.insert(p, Guess)

            if Wordlist == Displaylist:             # If user got every letter, end the game
                print(HangmanWord)
                print("Yay you won")
                Functions.EndingFunction()          # Run endingfunction
                exit()

            else:
                pass
        else:
            print("Hangman is getting closer to death....\n\n\n")   # if missed, print this
            Counter = Counter + 1       # death counter +1
            if Counter == 6:            # if death counter = 6, end the game
                Functions.HangmanGraphic(Counter)
                print("You killed him...")
                exit()
            else:
                pass


def DisplayFunction():          # ______ stuff
    global Display
    Display = ""
    for i in Displaylist:
        if i == " ":
            Display = Display + (" ") # add space where it is
        else:
            Display = Display + (i) # take whatever in displaylist in that position


# import stuff
import Functions
global Displaylist
Counter = 0
f = open("Hangman.txt", "r")
HangmanWord = (f.read()).upper()
f.close()
# make the letter into a list
Wordlist = list(HangmanWord)
UsedWords = []
#print underlines
Display = ""

for i in Wordlist:      # Make a display of unknown letters (_____)
    if i == " ":
        Display = Display + (" ")
    else:
        Display = Display + ("_")

Display = Display + ""
Displaylist = list(Display)

Functions.Menu()

Game = True
while Game == True:                 # main code running here
    Functions.HangmanGraphic(Counter)
    print("    [    " + Display + "    ]") # display it a bit cooler
    print("You've used: " + str(UsedWords))
    GuessFunction()
    DisplayFunction()







