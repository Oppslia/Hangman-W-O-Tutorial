word = "Blast Furnace Cooling Tower"
letterList = "abcdefghijklmnopqrstuvwxyz"
strikes = 0
guesses = 0
print("".join("_" if ord(x) != 32 else " " for x in word))
strikeAmount = 8
guessedLetters = []
dynamicString = "" #Defined here to avoid errors in line 38. Its to add consistancy.
def errorHandling(guess):
    try:
        int(guess)
        print("Intergers are an Invalid guess")
        return False
    except:
        pass
    if len(guess) < 1:
        return False
    if len(guess) > 1:
        print("Only guess one letter")
        return False
    if guess in guessedLetters:
        print(f"You already guessed {guess}")
    if ord(guess) not in range(97, 123):
        print("Invalid Input")
    else: 
        return True
while word != "completed" or strikes < (strikeAmount - 1):
     # creates a dynamic string to give user feedback
    guess = input("Guess your letter: ").lower()
    if guess.lower() == word.lower():
        guesses += 1
        break
    if errorHandling(guess) == True: #If the input is valid
        if guess not in word.lower(): # If the guess is not in the word
            strikes += 1 # Increments the amount of strikes
            guesses += 1 # Increments the amount of guesses
            letterList = letterList.translate({ord(str(guess)): None}) # Prints letters with spaces for easy reading
            guessedLetters.append(guess) # Adds wrong guesses to the list to prevent them from picking them again
            print(f'\n{guess} was not in the word | Strikes {f'{strikes}:{strikeAmount}'}\nAvailable letters:\n{" ".join(letterList)}\n')
            if len(dynamicString)>0: #If the string is not blank(Useful for first iterations if the first guess is wrong)
                print(dynamicString) 
            else: #If the string is blank(Only happens when guessing wrong before the first letter is guessed correctly)
                print("".join("_" if ord(x) != 32 else " " for x in word))# Prints "_" if the current letter in the word isn't a space else prints space
        elif guess in word.lower(): # If the guessed letter is in the word
            if guess in guessedLetters:
                pass
            else:
                guesses += 1 # Increments the amount of guesses
             
            dynamicString = "" # resets the string to blank for each guess
            for letter in word: # For each letter in the word
                
                if letter.lower() != guess: # If the letter(lowerform) is not = to the guess(already in lower form)
                    if letter.lower() in guessedLetters: # If the letter is in previously guessed letters(lower form)
                        dynamicString += letter # Adds correct letters to the dynamic string
                    elif ord(letter) == 32:
                        dynamicString += " "
                    else:
                        dynamicString += "_" # If the letter is doesnt meet above criteria a "_" is added to simulate a placeholder for an unguessed letter
                else: # If the letter is equal to the guess
                    dynamicString += letter # Adds the letter to the dynamic string
                    guessedLetters.append(letter.lower()) # Adds the letter to the guessed letters list to prevent picking the same letter twice in lower form
            print(dynamicString)# After the for loop concludes, prints the newly assembled dynamic string
           
            if dynamicString == word:
                break # If the dynamicString is == to the word it ends the game.
print(f"Congratulations! You guessed the word {word} within {guesses} tries, with {strikes} strikes out of {strikeAmount}")
                
                    
            