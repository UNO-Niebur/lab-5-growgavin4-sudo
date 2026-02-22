#Word Game is a knock-off version of a popular online word-guessing game.

import random

def inWord(letter, word):
    """Returns boolean if letter is anywhere in the given word"""
    for ch in word:
        if letter==ch:
            return True
    return False

def inSpot(letter, word, spot):
    correctLetter = word[spot]
    if letter == correctLetter:
        return True
    else:
        return False

def rateGuess(myGuess, word):

    """Rates your guess and returns a word with the following features.
    - Capital letter if the letter is in the right spot
    - Lower case letter if the letter is in the word but in the wrong spot
    - * if the letter is not in the word at all"""
    feedback = "" 

    for spot in range(5):
        myLetter = myGuess[spot]
        if inSpot(myLetter, word, spot) == True:
            feedback = feedback + myLetter.upper() #correct letter in location
        elif inWord(myLetter, word) == True:
            feedback = feedback + myLetter.lower() #correct letter in word, not location
        else:
            feedback=feedback + "*"

    return feedback

def main():
    #Pick a random word from the list of all words
    wordFile = open("words.txt", 'r')
    content = wordFile.read()
    wordList = content.split("\n")
    todayWord = random.choice(wordList)
    
    guessnum = 1
    while guessnum <= 6:
        validWord = False 
        while not validWord:
            guess = input(f"Enter guess #{guessnum}: ").lower()
            if guess not in wordList:
                print("Word not in word list.")
            else:
                validWord = True

        feedback = rateGuess(guess, todayWord)
        print(feedback)

        if guess == todayWord:
            print(f"Congratulations! You guessed the word in {guessnum} guesses!")
            break

        guessnum += 1  # increment after a valid guess

    else:
        print("Sorry! You ran out of guesses.")
        print("The word was", todayWord)

    print("Thanks for playing!")

if __name__ == '__main__':
    main()




if __name__ == '__main__':
  main()
