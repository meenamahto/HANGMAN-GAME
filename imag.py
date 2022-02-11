a=[''' 
       +------+
       |      |
              |
              |
              |
              |
              |
              ==========''','''
              
       +------+
       |      |
       0      |
              |
              |
              |
              |
              ==========
              ''','''
              
              
       +------+
       |      |
       0      |
      /       |
              |
              |
              |
              ==========
              ''','''
              
       +------+
       |      |
       0      |
      /|      |
              |
              |
              |
              ==========
              ''','''
       +------+
       |      |
       0      |
      /|\     |
              |
              |
              |
              ==========
              ''','''
              
       +------+
       |      |
       0      |
      /|\     |
       |      |
              |
              |
              ==========
              ''','''
              
       +------+
       |      |
       0      |
      /|\     |
       |      |
      /       |
              |
              ==========
              ''','''
              
       +------+
       |      |
       0      |
      /|\     |
       |      |
      / \     |
              |
              |
              ==========
              ''']







# for i in range(len(a)):
#     print(a[i])

# # from secrets import choice
# import string
# import random



# b=["meena","nono","nadini","meenamma"]
# def get_available_letters(letters_guessed):

#        # import string
#        all_letters = string.ascii_lowercase
#        letters_left = ""

#        for letter in all_letters:
#               if letter not in letters_guessed:
#                      letters_left += letter

#               return letters_left
# def get_guessed_word(secret_word,letters_guessed):
#     # print(letters_guessed)
#     index=0
#     guessed_word=""
#     while (index<len(secret_word)):
#         # print(secret_word[index])
#         if secret_word[index] in letters_guessed:
#             guessed_word+=secret_word[index]
#             # print(guessed_word)
#         else:
#             guessed_word+="_"
#         index+=1
#     return guessed_word

# def get_hint(secret_word, letters_guessed):

#        # import random
#        letters_not_guessed = []

#        index = 0
#        while (index < len(secret_word)):
#               letter = secret_word[index]
#               if letter not in letters_guessed:
#                      if letter not in letters_not_guessed:
#                             letters_not_guessed.append(letter)

#                      index += 1

#        return random.choice(letters_not_guessed)

# def is_word_guessed(secret_word, letters_guessed):


#        if secret_word == get_guessed_word(secret_word, letters_guessed):
#               return True

#        return False


# # while (True):
# #        available_letters = get_available_letters(letters_guessed)
# #        print ("Available letters: " + available_letters)

# #        guess = input("Please guess a letter: ")
# #        letter = guess.lower()

# #        if (not ifValid(letter))
# #               continue
# #               if letter in secret_word:
# #                      letters_guessed.append(letter)

# def ifValid(user_input):
#        if len(user_input) != 1:
#               return False

#        if not user_input.isalpha():
#               return False


#        return True
# '''
# secret_word: string, the secret word to guess.

# Hangman game yeh start karta hai:

# * Game ki shuruaat mei hi, user ko bata dete hai ki
#   secret_word mei kitne letters hai

# * Har round mei user se ek letter guess karne ko bolte hai

# * Har guess ke baad user ko feedback do ki woh guess uss
#   word mei hai ya nahi

# * Har round ke baar, user ko uska guess kiya hua partial word
#   display karo, aur underscore use kar kar woh letters bhi dikhao
#   jo user ne abhi tak guess nahi kiye hai

# # '''
# def hangman(secret_word):

#        print ("Welcome to the game, Hangman!")
#        print ("I am thinking of a word that is " + str(len(secret_word)) + " letters long.")
#        print ("")

#        letters_guessed = []
#        remainig_lives=8
#        while (True):
#               available_letters = get_available_letters(letters_guessed)
#               print ("Available letters: " + available_letters)

#               guess = input("Please guess a letter: ")
#               letter = guess.lower()

#               if letter in secret_word:
#                      letters_guessed.append(letter)
#                      print ("Good guess: " + get_guessed_word(secret_word, letters_guessed))
#                      print ("")

#                      if is_word_guessed(secret_word, letters_guessed) == True:
#                             print (" * * Congratulations, you won! * * ")
#                             print ("")
#                             break

#               else:
#                      print ("Oops! That letter is not in my word: " + get_guessed_word(secret_word,letters_guessed))
#                      letters_guessed.append(letter)
#                      print ("")
#                      print(a[8-remainig_lives])
#                      print()
#                      remainig_lives-+1
# secret=random.choice(b)
# hangman(secret)

