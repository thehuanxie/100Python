import random
import hangman_words, hangman_art

end_of_game = False
word_list = hangman_words.word_list
chosen_word = random.choice(word_list)
stages = hangman_art.stages
logo = hangman_art.logo

#TODO-1: - Create a variable called 'lives' to keep track of the number of lives left. 
#Set 'lives' to equal 6.
life = 6
guessed_word = set()

#Testing code
print(logo)

#Create blanks
display = []
for _ in chosen_word:
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    #Check guessed letter
    for position, letter in enumerate(chosen_word):
        if letter == guess:
            display[position] = letter
        
    
    #TODO-2: - If guess is not a letter in the chosen_word,
    #Then reduce 'lives' by 1. 
    #If lives goes down to 0 then the game should stop and it should print "You lose."
    if guess not in chosen_word and guess not in guessed_word:
        guessed_word.add(guess)
        life -= 1
        print(stages[life])
    else:
        print(f"{stages[life]}\n{guess} is already guessed")

    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    #TODO-3: - print the ASCII art from 'stages' that corresponds to the current number of 'lives' the user has remaining.
    if life == 0:
        print("Game over, you lose")
        break
    
