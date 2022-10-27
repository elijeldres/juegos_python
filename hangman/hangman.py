import random
from words_hangman import words
#from hangman_visual import lives_visual_dict
import string

def get_valid_word(words):
    word = random.choice(words)                 # choose a random word from the list in words_hagman.py file
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word.upper()


def hangman():
    word = get_valid_word( words)  
    word_letters = set(word)                     # letters valid in the word
    alphabet = set(string.ascii_uppercase)       # making it upper, for no deal with format.  
    used_letters = set()                         # letters that the user has used ( guess)

    lives = 10                                      

    # GAME INSTRUTION
    print(' GAME INSTRUTION: \p Fill the letter in the blanks (-) if the player guess correctly, when the player guess wrong a life is taken, you have 10 lifes. \pHAVE FUN !!! ')
    
    # guetting input from user

    while len(word_letters) > 0 and lives > 0 :  
        # letters used by user (guess)
        # ' '.join(['a', 'b', 'c')--> a b c 
        print('You have', lives, 'lives left. You already have used these letters: ', ' '.join(used_letters))

        # what current word is ( ie W - R D)
        word_list = [letter if letter in used_letters else '-' for letter in word]
        #print(lives_visual_dict[lives])
        print('Current word: ',' '.join(word_list))

          
        user_letter = input('Type a letter to guess the word: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters: 
                word_letters.remove(user_letter)
            
            else:
                lives = lives -1                # remove a life when the choosen letter is wrong
                print('UPS! a life has been taken. That letter is not used in the guessing word. Please try again')

        elif user_letter in used_letters:
            print('\nYou have already used that letter, please try a diferent one')
                
        else:
            print('\nThat is not a valid letter.')

    # gets here when len(word_letters) == 0 or when lives == 0

    if lives == 0:
       #print(lives_visual_dict[lives])
        print('you died, sorry. The word was: ', word)
    else:
        print('YOU ARE THE WORD MASTER, the word was', word, '!!!')

if __name__ == '__main__':

    hangman()



