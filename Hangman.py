secretWord = "pasadena"

#Empty list for letters that have been guessed
lettersguessed = ""

#How many times you can be wrong. Exremely Hard >:)
failurecount = 3

while failurecount > 0:

    guess = input("Pick a letter to guess with")

    if guess in secretWord:

        print("Good Job! Keep on guessing")
    else:
        failurecount -= 1
        print("Incorrct guess! Try Again")

#Maintains all the guessed letters that have already been guessed in a list... IDK
    lettersguessed = lettersguessed + guess
    wronglettercounter = 0
#The f in the print are for the {}
    for letter in secretWord:
        if letter in lettersguessed:
            print(f"{letter}", end="")
        else:
            print("_", end="")
            wronglettercounter += 1

    if wronglettercounter == 0:
        print(f" Nice Work! The secret word was: {secretWord}!")
        break
else:
    print("Sorry you didn't find the secret word :(")