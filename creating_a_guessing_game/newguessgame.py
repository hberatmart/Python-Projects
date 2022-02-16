import random
print("hello, welcome to the my game!")
def guessGame():
    randNum = random.randint(0, 10)
    print(randNum)

    guessNum = 3
    while guessNum:
        userGuess = int(input("guess a number between 0 to 10"))
        if userGuess == randNum:
            userChoice = input("you guessed correct. would you like to play again my game?? (yes for again)")
            if userChoice.lower() == "yes":
                guessGame()
            else:
                print("goodbye")
        else:
            if guessNum == 1:
                loseChoise = input("you used your 3 chances and you have no more chance. do you wanna play again ?")
                if loseChoise.lower() == "yes":
                    guessGame()
                else:
                    print("goodbye")
                    exit()
            print("you guessed wrong try again")
            guessNum = guessNum - 1

guessGame()