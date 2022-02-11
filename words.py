

# import string
import random
def load_word():
    w="words.txt"
    inf=open(w,"r")
    l=inf.readline()
    word_list=l.split()
    return word_list
    # print(word_list)


def choose_word():
    word_list=load_word()
    secret_word=random.choice(word_list)
    secret_word=secret_word.lower()
    return secret_word
    

