import string
import random
from imag import a
from words import choose_word



def hangman(secret_word):

    print("welcome to the game,Hangman!")
    print("I am thinking of a word that is "+str(len(secret_word))+" letters")
    print("")

    letters_guessed=[]
    total_lives=remaining_lives=8
    level=input("Enter your level:-\n'a' for easy\n'b' for mediem\n'c' for hard")
    images_selection=[0,1,2,3,4,5,6,7]
    if level=="b":
        total_lives=remaining_lives=6
        images_selection=[1,2,3,4,6,7]
    elif level=="c":
        total_lives=remaining_lives=4
        images_selection=[1,3,5,7]
    else:
        if level!="a" or level!="b" or level!="c":
            print("your enter is invalid")
            
            # level=input("Enter your level:-\n'a' for easy\n'b' for mediem\n'c' for hard")

    hit=0
    while (remaining_lives>0):
        letters_left=string.ascii_lowercase
        for i in letters_guessed:
            letters_left=letters_left.replace(i,"")
        print("available letters="+letters_left)
        guess=input("please guess a letter:")
        letter=guess.lower()
        if guess=="hint":
            if hit==0:
                letters_not_guessed=[]
                index=0
                while (index<len(secret_word)):
                    let=secret_word[index]
                    if let not in letters_guessed:
                        if let not in letters_not_guessed:
                            letters_not_guessed.append(let)
                    index+=1
                p=random.choice(letters_not_guessed)
                print("your hint for next character",p)
                hit=1
                continue


        if (not (letter.isalpha()) or (len(letter)!=1)) :
            print("invalid input")
            continue
        

        if letter in secret_word:
            letters_guessed.append(letter)
            index=0
            guessed_word=""
            while (index<len(secret_word)):
                if secret_word[index] in letters_guessed:
                    guessed_word+=secret_word[index]
                else:
                    guessed_word+="_"
                index+=1
                
            print("Good guess:"+ guessed_word)
            print("")
            if secret_word==guessed_word:
                print("* * Congratulations,you won! * *")
                print("")
                break
        else:
            index=0
            guessed_word=""
            while (index<len(secret_word)):
                if secret_word[index] in letters_guessed:
                    guessed_word+=secret_word[index]
                else:
                    guessed_word+="_"
                index+=1
            print("Oops! That letter is not in my word:"+ guessed_word)
            print(a[images_selection[total_lives-remaining_lives]])
            remaining_lives-=1
            print("Remaining lives=",remaining_lives)
            print("")
    else:
        print("sorry!,you ran out of guesses.The word was=",str(secret_word))

secret_word=choose_word()
hangman(secret_word)



# from words import load_word
# load_word()


