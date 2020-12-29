import turtle
import random
def scramble(w):
    letters = list(w)
    random.shuffle(letters)
    scramble = ''
    for i in letters:
        scramble_word = scramble_word + i
    return scramble_word

scramble('airplane')
