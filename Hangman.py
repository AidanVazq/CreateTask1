
import random
#^^^^^^^^^ Im not sure what that does I just looked at what W3 schools put and it worked I guess.

SecretList = ["pasadena", "roseparade", "trombone", "california", "computer", "science", "advanced", "placement", "exam"]

secretWord = random.choice(SecretList)

#Because empty for letters that have been guessed
lettersguessed = ""

#How many times you can be wrong. Exremely Hard >:)
lives = 3

while lives > 0:

    guess = input("Pick a letter to guess with")

    if guess in secretWord:

        print("Good Job! Keep on guessing")
    else:
        lives -= 1
        print("Incorrct guess! Try Again")

#Maintains all the guessed letters that have already been guessed. (STORES THEM UP ABOVE IN LETTERSGUESSED) I THINK...
    lettersguessed = lettersguessed + guess
    wronglettercounter = 0
#The f in the print are for the {}
    for letter in secretWord:
        if letter in lettersguessed:
            print(f"{letter}", end="")
        else:
            print("_", end="")
            wronglettercounter += 1 
    # ^^^^^^^^^ (Definition to HELP me understand end paramters) The end parameter in the print function is used to add any string
    # At the end of the output of the print statement in python.
    if wronglettercounter == 0:
        print(f" Nice Work! The secret word was: {secretWord}!")
        break
else:
    print("Sorry you didn't find the secret word :(")