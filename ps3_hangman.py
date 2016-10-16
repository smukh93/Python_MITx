# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    if lettersGuessed == []:
        return False
    for word in secretWord:
        resultList = []
        for letter in lettersGuessed:
            result = (word == letter)
            resultList.append(result)
        if True in resultList:
            continue
        else:
            return False
    return True
#secretWord = 'apple' 
#lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
#print(isWordGuessed(secretWord, lettersGuessed))
#print(isWordGuessed('banana', ['z', 'x', 'q', 'b', 'a', 'n', 'a', 'n', 'a']))

def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    result = ""
    for word in secretWord:
        if word in lettersGuessed:
            result+=word
        else:
            result+="_"
    return result
secretWord = 'apple' 
lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
print(getGuessedWord(secretWord, lettersGuessed))

import string
def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    all_letter = list(string.ascii_lowercase)
    available_letter = ""
    for letter in lettersGuessed:
        all_letter.remove(letter)
    for char in all_letter:
        available_letter+=char
    return available_letter
    
lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
print(getAvailableLetters(lettersGuessed))
    
'''
def hangman(secretWord):
    ''''''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
   
    # FILL IN YOUR CODE HERE...
    import string 
    initialString = string.ascii_lowercase
    print("Welcome to Hangman!")
    print("I am guessing a "+ str(len(secretWord)) +" lettered word!")
    get_letter = ""
    trials = 8
    guessedLetters = ""
    while trials > 0:
        if isWordGuessed(secretWord,get_letter):
            print ('Congratulations,you won')
            break
        print ('You have ' + str(trials) + ' guesses left.')
        print ("available letters:  "+ getAvailableLetters(guessedLetters))
        char = input("Guess a letter:  ")
        lo_char = char.lower()
        get_letter+=(char.lower())
        outString = getGuessedWord(secretWord,get_letter)
        if lo_char in secretWord:
            if lo_char in guessedLetters:
                print ("Oops! You already guessed that letter! " +outString)
            else:
                print ("Good Going!" +outString)
        else:
            if lo_char in guessedLetters:
                print ("Oops! You already guessed that letter! "+outString)
            else:
                print ("Letter not in the secretWord"+outString)
                trials-=1
        guessedLetters+=lo_char
    if trials == 0 :
        print ("Sorry! You can't guess anymore. The secretword was"
        + secretWord+".")
    
        

''' 
def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.
    Starts up an interactive game of Hangman.
    * At the start of the game, let the user know how many 
      letters the secretWord contains.
    * Ask the user to supply one guess (i.e. letter) per round.
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.
    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.
    Follows the other limitations detailed in the problem write-up.  '''
    
    import string
    initialString = string.ascii_lowercase
    print ('Welcome to the game, Hangman!')
    print ('I am thinking of a word that is ' + str(len(secretWord)) + ' letters long.')
    print ('-------------')
    getLetter = ''
    num = 8
    print ('You have 8 guesses left.')
    print ('Available letters: ' + str(initialString))
    getLetterList = ''
    while num <= 8 and num >= 0:
##        print 'You have ' + str(num) + ' guesses left.'
##        if num == 8:
##            print 'Available letters: ' + str(initialString)
##        else:
##            print 'Available letters: ' + getAvailableLetters(outString)
        

        char = input('Please guess a letter: ')
        loChar = char.lower()
        getLetter += loChar

##        print 'getLetter is ' + getLetter
##        print 'getLetterList is ' + getLetterList


        outString = getGuessedWord(secretWord, getLetter)

        leftLetters = getAvailableLetters(getLetter)
        
        result = isWordGuessed(char, secretWord)

        if result == True:
            if char in getLetterList:
                print ('Oops! You\'ve already guessed that letter: ' + outString)
            
            else:
                print ('Good guess: ' + outString)
                getLetterList += getLetter
                
            print ('-------------')
            if outString == secretWord:
                print ('Congratulations, you won!')
                break
                
            print ('You have ' + str(num) + ' guesses left.')
            print ('Available letters: ' + getAvailableLetters(outString))
            
            
        else:
            if char in getLetterList:
                print ('Oops! You\'ve already guessed that letter: ' + outString)
                print ('-------------')
                print ('You have ' + str(num) + ' guesses left.')
                print ('Available letters: ' + leftLetters)
            else:
                print ('Oops! That letter is not in my word: ' + outString)
                getLetterList += getLetter
                print ('-------------')
            
                if num != 1:
                    num -= 1
                    print ('You have ' + str(num) + ' guesses left.')
                    print ('Available letters: ' + leftLetters)
                else:
                    print ('Sorry, you ran out of guesses. The word was ' + secretWord + '.')
                    break




# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
